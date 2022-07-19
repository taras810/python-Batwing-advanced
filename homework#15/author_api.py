import http

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import db
from models.author import Author
from serializers.author import AuthorSchema

author_router = Blueprint('author', __name__, url_prefix='/author')


@author_router.route('')
def get():
    author_schema = AuthorSchema()

    authors = Author.query.order_by(Author.name)
    authors_json = author_schema.dump(authors, many=True)
    return jsonify(authors_json)


@author_router.route('/<int:id_>')
def retrieve(id_):
    author_schema = AuthorSchema()
    author = Author.query.filter_by(id=id_).first()
    authors_json = author_schema.dump(author)
    return jsonify(authors_json)


@author_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = AuthorSchema()
    try:
        author_data = schema.load(data)
        new_author = Author(name=author_data['name'])
        db.session.add(new_author)
        db.session.commit()

        new_author_json = schema.dump(new_author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = AuthorSchema()
    try:
        author_data = schema.load(data)
        author = Author.query.filter_by(id=id_).first()
        author.title = author_data['name']
        db.session.add(author)
        db.session.commit()

        new_author_json = schema.dump(author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Author.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
