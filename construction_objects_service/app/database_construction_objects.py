from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///constructionSupervision.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class ConstructionObjectOrm(Model):
    __tablename__ = 'construction_objects'

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    type: Mapped[str | None]

    violations = relationship("ViolationOrm", back_populates="construction_object")

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
