from sqlalchemy import select, update, delete

from database_construction_objects import ConstructionObjectOrm, new_session
from schemas_construction_objects import SConstructionObjectAdd, SConstructionObject


class ConstructionSupervisionRepository:
    @classmethod
    async def add_construction_object(cls, construction_object: SConstructionObjectAdd) -> int:
        async with new_session() as session:
            data = construction_object.model_dump()
            new_construction_object = ConstructionObjectOrm(**data)
            session.add(new_construction_object)
            await session.flush()
            await session.commit()
            return new_construction_object.id

    @classmethod
    async def get_all_construction_objects(cls) -> list[SConstructionObject]:
        async with new_session() as session:
            query = select(ConstructionObjectOrm)
            result = await session.execute(query)
            construction_object_models = result.scalars().all()
            construction_object_schemas = [SConstructionObject.model_validate(construction_object_model) for
                                           construction_object_model in construction_object_models]
            return construction_object_schemas
