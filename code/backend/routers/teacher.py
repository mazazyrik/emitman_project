from fastapi import APIRouter

from schemas.teacher_schemas import (
    TeacherGetSchema, TeacherPostSchema
)
from db import Teacher

router = APIRouter(prefix='/teacher', tags=['teacher'])


@router.get('/', response_model=list[TeacherGetSchema])
async def get_teachers():
    return await Teacher.all()


@router.get('/{decanat_name}', response_model=list[TeacherGetSchema])
async def get_decanat_teachers(decanat_name: str):
    return await Teacher.filter(decanat__name=decanat_name)


@router.post('/', response_model=TeacherGetSchema)
async def create_teacher(teacher: TeacherPostSchema):
    return await Teacher.create(**teacher.dict())


@router.get('/{teacher_name}', response_model=TeacherGetSchema)
async def get_teacher(teacher_name: str):
    return await Teacher.get(name=teacher_name)
