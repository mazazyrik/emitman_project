from pydantic import BaseModel
from teacher_schemas import TeacherGetSchema


class GroupGetSchema(BaseModel):
    name: str


class DecanatGetSchema(BaseModel):
    name: str
    contacts: str
    teachers: list[TeacherGetSchema]


class DecanatGroupGetSchema(BaseModel):
    name: str
    groups: list[GroupGetSchema]
