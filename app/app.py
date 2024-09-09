import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from common import create_db, logger
from resource.user import router as user_router


@asynccontextmanager
async def lifespan(app_: FastAPI):
    logger.info("Running task before service starts")
    await create_db()
    yield
    # # Code to run after the application stops (optional)
    # await some_cleanup_task()


app = FastAPI(
    title='REST API Demo',
    description='Simple demo using FastAPI',
    version='v0.1',
    contact={'email': 'john.doe@gmail.com'},
    redoc_url='/redoc',
    docs_url='/docs',
    openapi_url='/openapi',
    lifespan=lifespan
)
app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=6180, reload=True)
