from fastapi import APIRouter, Depends, HTTPException

from repository import ConstructionSupervisionRepository
from schemas_construction_objects import SConstructionObjectAdd, SConstructionObject, SConstructionObjectId

router = APIRouter()

construction_object_router = APIRouter(
    prefix="/construction_object",
    tags=["Объекты Строительства"],
)


@construction_object_router.post("")
async def add_construction_object(construction_object: SConstructionObjectAdd) -> SConstructionObjectId:
    new_construction_object_id = await ConstructionSupervisionRepository.add_construction_object(construction_object)
    return {"id": new_construction_object_id}


@construction_object_router.get("")
async def get_all_construction_objects() -> list[SConstructionObject]:
    construction_objects = await ConstructionSupervisionRepository.get_all_construction_objects()
    return construction_objects


router.include_router(construction_object_router)

