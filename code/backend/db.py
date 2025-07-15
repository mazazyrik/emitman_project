from tortoise import fields
from tortoise.models import Model
from enum import Enum

# utils


class ProgramName(str, Enum):
    OPI = 'Отделение прикладной информатики'
    OMES = 'Отделение международного экономического сотрудничества'
    OE = 'Отделение экономики'
    ONE = 'Отделение национальной экономики'
    BI = 'Отдеделение бизнес-информатики'
    ONLINE = 'Онлайн-программы'
    IT_MANAGMENT = 'Школа IT-менеджмента'

# models


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    surname = fields.CharField(max_length=50)
    father_name = fields.CharField(max_length=50)
    is_activist = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    telegram_id = fields.BigIntField(unique=True, null=True)
    group_id = fields.ForeignKeyField('db.Group', related_name='users')
    grade = fields.IntField(default=1)
    program = fields.CharEnumField(enum_type=ProgramName, null=False)
    brs_rate = fields.IntField(default=0)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Admin(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=50)
    name = fields.CharField(max_length=50)
    surname = fields.CharField(max_length=50)
    is_ss = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    def __str__(self):
        return self.name


class Decanat(Model):
    id = fields.IntField(pk=True)
    name = fields.CharEnumField(enum_type=ProgramName, null=False)
    contacts = fields.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    program = fields.CharEnumField(enum_type=ProgramName, null=False)
    mail = fields.CharField(max_length=50, null=False)
    decanat = fields.ForeignKeyField('db.Decanat', related_name='teachers')

    def __str__(self):
        return self.name


class Group(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=False)
    decanat = fields.ForeignKeyField('db.Decanat', related_name='groups')

    def __str__(self):
        return self.name
