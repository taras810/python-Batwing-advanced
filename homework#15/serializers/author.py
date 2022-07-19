from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name = fields.String(required=True)
