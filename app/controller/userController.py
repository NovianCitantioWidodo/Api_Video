from app.model.user import User
from app import response, app, db
from flask import request
import datetime
from flask_jwt_extended import create_access_token, create_refresh_token

def index():
    try:
        user = User.query.all()
        data = listObject(user)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def listObject(data):
    datas = [singleObject(i) for i in data]
    return datas

def singleObject(data):
    datas = {
        'id': data.id,
        'email': data.email
    }
    return datas

def detail(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "Tidak ada data")
        else:
            data = singleObject(user)
            return response.success(data, "success")

    except Exception as e:
        print(e)

def signup():
    try:
        user = User( 
            email       = request.form.get('email'))
        user.setPassword(
            password = request.form.get('password'))

        data = singleObject(user)
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        db.session.add(user)
        db.session.commit()

        return response.success({
            "email": user.email,
            "access_token": access_token,
            "refresh_token": refresh_token
        }, "Sukses menambahkan data")

    except Exception as e:
        print(e)

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Email tidak terdaftar')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'Kombinasi password salah')
        
        data = singleObject(user)
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        
        return response.success({
            "email": user.email,
            "access_token": access_token,
            "refresh_token": refresh_token
        }, "Sukses login")
    
    except Exception as e:
        print(e)

def update(id):
    try:
        user = User.query.filter_by(id=id).first()
        user.email = request.form.get('email')
        user.setPassword(
            password = request.form.get('password'))

        data = singleObject(user)
        db.session.commit()
        return response.success(data, 'Sukses merubah data')
    
    except Exception as e:
        print(e)

def delete(id):
    try:
        user = User.query.filter_by(id=id).first()
        data = singleObject(user)
        db.session.delete(user)
        db.session.commit()
        return response.success(data, 'Data telah dihapus')
    
    except Exception as e:
        print(e)