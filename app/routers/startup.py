import os

from fastapi import APIRouter
from app.core.settings import get_settings

router = APIRouter()


@router.on_event("startup")
def startup():
    if get_settings().api_debug is True:
        os.system('python -m pytest')
