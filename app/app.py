from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database.start import create_db
from resource.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run before the application starts
    print("Running task before service starts")
    # Example: Initialize database connection or perform a startup task
    await create_db()

    yield  # This point allows the app to start running

    # # Code to run after the application stops (optional)
    # print("Running task after service stops")
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


@app.get("/")
def read_root():
    return {"Hello": "World!"}


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=6180, reload=True)