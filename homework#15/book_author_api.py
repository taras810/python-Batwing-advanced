import http
from flask import Blueprint, jsonify, request
from models.book_author import BookAuthor
from models.book import Book
from models.author import Author
from database import db
from serializers.book_author import BookAuthorSchema

book_author = Blueprint("book_author", __name__, url_prefix='/book_author')


@book_author.route('')
def get():
    b_a = BookAuthor.query.all()
    b_a_json = BookAuthorSchema().dump(b_a, many=True)
    return jsonify(b_a_json)


@book_author.route('/<int:id_>')
def retrieve(id_):
    b_a = BookAuthor.query.filter_by(id=id_).first()
    b_a_json = BookAuthorSchema().dump(b_a)
    return jsonify(b_a_json)


@book_author.route('/<int:book_id>/<int:author_id>')
def create(book_id, author_id):
    if Book.query.filter(
            Book.id == book_id).first() and Author.query.filter(
            Author.id == author_id).first():
        new_relation = BookAuthor(book_id=book_id, author_id=author_id)
        db.session.add(new_relation)
        db.session.commit()
        new_relation_json = BookAuthorSchema().dump(new_relation)
        return jsonify(new_relation_json), http.HTTPStatus.CREATED
    else:
        return 'BAD ID', http.HTTPStatus.BAD_REQUEST


@book_author.route('', methods=['PUT'])
def update():
    data = request.get_json(force=True)

    if b_a := BookAuthor.query.filter_by(id=data["id"]).first():
        b_a.book_id, b_a.author_id = data["book_id"], data["author_id"]
        db.session.add(b_a)
        db.session.commit()
        b_a_update = BookAuthorSchema().dump(b_a)
        return jsonify(b_a_update)
    else:
        return 'BAD ID', http.HTTPStatus.BAD_REQUEST


@book_author.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    BookAuthor.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT