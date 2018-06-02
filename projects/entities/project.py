from marshmallow import Schema, fields

from projects.entities.links import LinksSchema


class ProjectSchema(Schema):
    id = fields.UUID(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str(required=True)
    links = fields.Nested(LinksSchema, required=True)
