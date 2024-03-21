from fastapi import FastAPI
from contextlib import asynccontextmanager

from router import router as construction_supervision_router
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)
app.include_router(construction_supervision_router)

