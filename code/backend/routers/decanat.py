from fastapi import APIRouter
from schemas.teacher_schemas import TeacherGetSchema
from db import Decanat
from schemas.decanat_schemas import DecanatGetSchema, DecanatGroupGetSchema

router = APIRouter(prefix="/api/decanat", tags=["decanat"])


@router.get("/all")
def get_decanats() -> DecanatGroupGetSchema:
    all_decs = Decanat.all().prefetch_related('groups')

    decs_with_groups_list = [
        DecanatGroupGetSchema(
            name=dec.name,
            groups=[group.name for group in dec.groups]
        ) for dec in all_decs
    ]

    return decs_with_groups_list


@router.get("/all/{decanat_name}")
def get_decanat_with_group(decanat_name: str) -> DecanatGroupGetSchema:
    dec = Decanat.get(name=decanat_name)
    return DecanatGroupGetSchema(
        name=dec.name,
        groups=[group.name for group in dec.groups]
    )


@router.get('/{decanat_name}')
def get_decanat(decanat_name: str) -> DecanatGetSchema:
    dec = Decanat.get(name=decanat_name).prefetch_related('teachers')

    return DecanatGetSchema(
        name=dec.name,
        contacts=dec.contacts,
        teachers=[TeacherGetSchema(
            name=teacher.name,
            program=teacher.program,
            mail=teacher.mail
        ) for teacher in dec.teachers]
    )
