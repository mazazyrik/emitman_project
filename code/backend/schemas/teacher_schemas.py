from pydantic import BaseModel
from db import ProgramName


class TeacherGetSchema(BaseModel):
    name: str
    program: ProgramName
    mail: str


class TeacherPostSchema(BaseModel):
    name: str
    program: ProgramName
    mail: str
    decanat: int
