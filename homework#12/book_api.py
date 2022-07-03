import http

from flask import Blueprint, Response, request

from db.book_db import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    books = db.get_all()
    return Response(str(books))
