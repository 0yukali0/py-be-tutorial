from fastapi import FastAPI
from routers.handleFunc import router

app = FastAPI()

app.include_router(router)