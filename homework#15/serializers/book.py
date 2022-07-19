from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    title = fields.String(required=True)
    page_length = fields.Integer(required=True)
