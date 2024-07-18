from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables

from router import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("DB is ready to use")
    print("server is working now")
    yield
    print("server isn't working now")
    # await delete_tables()
    # print("DB is clean")


app = FastAPI(lifespan=lifespan)

app.include_router(task_router)
