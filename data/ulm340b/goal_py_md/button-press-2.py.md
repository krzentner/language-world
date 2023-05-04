

You can use the following variables in your program:
 - `robot`
 - `button`
 - `the robot's gripper`
 - `button`
"""
[eod] [code]from typing import Sequence
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import TextAsFrom
from app import crud, models
from . import schemas
from app.schemas import commons_response
from .utils import create_db_context
from app.oauth2 import get_current_user
from app.router import oauth_router, token_router

router = APIRouter()


@router.get("/items/", response_model=commons_response)
async def read_items(db: AsyncSession = Depends(create_db_context)):
    return crud.item.get_multi(db=db)


@router.get("/items/{id}", response_model=commons_response)
async def read_item(id: int, db: AsyncSession = Depends(create_db_context)):
    return crud.item.get(db=db, id=id)


@router.post("/items/", response_model=commons_response)
async def create_item(
        item: schemas.ItemCreate,
        db: AsyncSession = Depends(create_db_context)
):
    return crud.item.create(db=db, obj_in=item)


@router.put("/items/{id}", response_model=commons_response)
async def update_item(
        id: int,
        item: schemas.ItemUpdate,
        db: AsyncSession = Depends(create_db_context)
):
    return crud.item.update(db=db, db_obj=id, obj_in=item)


@router.delete("/items/{id}", response_model=commons_response)
async def delete_item(
        id: int,
        db: AsyncSession = Depends(create_db_context)
):
    return crud.item.remove(db=db, id=id)


@router.post("/items/{item_id}/like", response_model=commons_response)
async def like_item(
        item_id: int,
        like: schemas.LikeCreate,
        user: models.User = Depends(get_current_user),
        db: AsyncSession = Depends(create_db_context)
):
    return crud.like.create(db=db, item_id=item