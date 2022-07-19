from marshmallow import Schema, fields

from serializers.book import BookSchema
from serializers.author import AuthorSchema


class BookAuthorSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    authors = fields.Nested(AuthorSchema())
    books = fields.Nested(BookSchema())
