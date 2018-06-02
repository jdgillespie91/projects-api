from marshmallow import Schema, fields


class LinksSchema(Schema):
    homepage = fields.Url(schemes={'https'})
