from tortoise import fields

from .base import TortoiseModel


class School(TortoiseModel):
    name = fields.CharField(max_length=200, index=True)
    address = fields.CharField(max_length=255, unique=True, index=True)
    phone = fields.CharField(max_length=255, index=True, unique=True)
    fax = fields.CharField(max_length=255, index=True, unique=True, null=True)
    email = fields.CharField(max_length=255, index=True, unique=True)
    site_url = fields.CharField(max_length=255, null=True)
