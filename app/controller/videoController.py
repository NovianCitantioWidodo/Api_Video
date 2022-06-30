from app.model.video import Video
from app import response, app, db
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token

def index():
    try:
        video = Video.query.all()
        data = listObject(video)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def listObject(data):
    datas = [singleObject(i) for i in data]
    return datas

def singleObject(data):
    datas = {
        'id': data.id,
        'name': data.name, 
        'views': data.views,
        'likes': data.likes,
        # 'owner': data.owner
    }
    return datas

def detail(id):
    try:
        video = Video.query.filter_by(id=id).first()
        if not video:
            return response.badRequest([], "Tidak ada data")
        else:
            data = singleObject(video)
            return response.success(data, "success")

    except Exception as e:
        print(e)

def add():
    try :
        video = Video(
            name=request.form.get('name'),
            views=request.form.get('views'),
            likes=request.form.get('likes'))
        
        data = singleObject(video)
        db.session.add(video)
        db.session.commit()
        return response.success({
            'name': data['name'], 
            'views': data['views'],
            'likes': data['likes']
        }, 'Sukses menambahkan data')
    
    except Exception as e:
        print(e)

def update(id):
    try:
        video = Video.query.filter_by(id=id).first()
        video.name = request.form.get('name')
        video.views = request.form.get('views')
        video.likes = request.form.get('likes')
        # video.owner = request.form.get('owner')

        data = singleObject(video)
        db.session.commit()
        return response.success(data, 'Sukses merubah data')
    
    except Exception as e:
        print(e)

def delete(id):
    try:
        video = Video.query.filter_by(id=id).first()
        data = singleObject(video)
        db.session.delete(video)
        db.session.commit()
        return response.success(data, 'Data telah dihapus')
    
    except Exception as e:
        print(e)