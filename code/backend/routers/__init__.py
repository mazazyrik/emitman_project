from fastapi import APIRouter
from .decanat import router as decanat_router
from .teacher import router as teacher_router

core_router = APIRouter()

core_router.include_router(decanat_router)
core_router.include_router(teacher_router)
