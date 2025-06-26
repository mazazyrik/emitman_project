from tortoise import fields
from tortoise.models import Model
from enum import Enum

# utils


class ProgramName(str, Enum):
    OPI = 'opi'
    OMES = 'omes'
    OE = 'oe'
    ONE = 'one'
    BI = 'bi'
    ONLINE = 'online'
    IT_MANAGMENT = 'it-management'

# models


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    surname = fields.CharField(max_length=50)
    father_name = fields.CharField(max_length=50)
    is_activist = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    telegram_id = fields.BigIntField(unique=True, null=True)
    group_id = fields.CharField(max_length=50, null=False)
    grade = fields.IntField(default=1)
    program = fields.CharEnumField(enum_type=ProgramName, null=False)
    brs_rate = fields.IntField(default=0)

    def __str__(self):
        return self.username


class Admin(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    surname = fields.CharField(max_length=50)
    is_ss = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    def __str__(self):
        return self.username