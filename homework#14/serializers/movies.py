from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    title = fields.String(required=True)
