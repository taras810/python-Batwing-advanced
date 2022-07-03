import http

from flask import Blueprint, Response, request

from db.db import UserDB

user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
def get():
    users = db.get_all()
    return Response(str(users))


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    return user


@user_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    new_user = db.add(name, email, password)

    if new_user:
        return new_user, http.HTTPStatus.CREATED
    else:
        return "This user alredy exists", http.HTTPStatus.BAD_REQUEST


@user_router.route('', methods=['PUT'])
def update():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    updated_user = db.update_by_email(email, name, password)

    if updated_user:
        return updated_user, http.HTTPStatus.CREATED
    else:
        return "The data you passed is incorrect", http.HTTPStatus.BAD_REQUEST


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    db.delete_by_email(email)
    return {}, http.HTTPStatus.NO_CONTENT
