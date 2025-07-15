from fastapi import APIRouter
from schemas.teacher_schemas import TeacherGetSchema
from db import Decanat
from schemas.decanat_schemas import DecanatGetSchema, DecanatGroupGetSchema

router = APIRouter(prefix='/decanat', tags=['decanat'])


@router.get('/all')
async def get_decanats() -> list[DecanatGroupGetSchema]:
    all_decs = await Decanat.all().prefetch_related('groups')

    decs_with_groups_list = [
        DecanatGroupGetSchema(
            name=dec.name,
            groups=[{"name": group.name} for group in dec.groups]
        ) for dec in all_decs
    ]

    return decs_with_groups_list


@router.get('/all/{decanat_name}')
async def get_decanat_with_group(decanat_name: str) -> DecanatGroupGetSchema:
    dec = await Decanat.get(name=decanat_name).prefetch_related('groups')
    return DecanatGroupGetSchema(
        name=dec.name,
        groups=[{"name": group.name} for group in dec.groups]
    )


@router.get('/{decanat_name}')
async def get_decanat(decanat_name: str) -> DecanatGetSchema:
    dec = await Decanat.get(name=decanat_name).prefetch_related('teachers')

    return DecanatGetSchema(
        name=dec.name,
        contacts=dec.contacts,
        teachers=[TeacherGetSchema(
            name=teacher.name,
            program=teacher.program,
            mail=teacher.mail
        ) for teacher in dec.teachers]
    )


@router.post('/{decanat_name}')
async def create_decanat(decanat_name: str):
    return await Decanat.create(name=decanat_name)


@router.delete('/{decanat_name}')
async def delete_decanat(decanat_name: str):
    return await Decanat.filter(name=decanat_name).delete()


@router.put('/{decanat_name}')
async def update_decanat(decanat_name: str):
    return await Decanat.filter(name=decanat_name).update(name=decanat_name)
