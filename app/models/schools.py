from tortoise import fields

from .base import TortoiseModel


class School(TortoiseModel):
    area = fields.CharField(max_length=255)
    city = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=255, index=True, unique=True)
    fax = fields.CharField(max_length=255, index=True, unique=True)
    email = fields.CharField(max_length=255, index=True, unique=True)
    site_url = fields.CharField(max_length=255, null=True)
