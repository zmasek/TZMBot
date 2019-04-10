from tortoise.models import Model
from tortoise import fields


class Biography(Model):
    id = fields.IntField(pk=True)
    person = fields.TextField(unique=True)
    content = fields.TextField(null=True)

    def __str__(self):
        return self.person
