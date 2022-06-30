from app import app, response
from flask import request, jsonify
from app.controller import videoController, userController
from flask_jwt_extended import jwt_required, get_jwt_identity, unset_jwt_cookies

@app.route('/')
def index():
    return 'home'

@app.route('/api/user/signup', methods=['GET', 'POST'])
def user_signup():
    if request.method == 'GET':
        return 'signup'
    elif request.method == 'POST':
        return userController.signup()

@app.route('/api/user/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':
        return 'login'
    elif request.method == 'POST':
        return userController.login()

@app.route("/api/logout", methods = ["POST"])
def user_logout():
    del_response = jsonify({
        "message": "logout successful"
    })
    unset_jwt_cookies(del_response)
    return del_response

@app.route('/api/user-all', methods=['GET'])
@jwt_required()
def user_all():
    return userController.index()


@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protect():
    current_user = get_jwt_identity()
    return response.success(current_user, "Sukses")


@app.route('/api/user/<id>', methods=['GET', 'PUT', 'DELETE'])
# @jwt_required()
def user_id(id):
    if request.method == 'GET':
        return userController.detail(id)
    elif request.method == 'PUT':
        return userController.update(id)
    if request.method == 'DELETE':
        return userController.delete(id)

@app.route('/api/video', methods=['GET', 'POST'])
# @jwt_required()
def video():
    if request.method == 'GET':
        return videoController.index()
    elif request.method == 'POST':
        return videoController.add()

@app.route('/api/video/<id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def video_id(id):
    if request.method == 'GET':
        return videoController.detail(id)
    elif request.method == 'PUT':
        return videoController.update(id)
    if request.method == 'DELETE':
        return videoController.delete(id)