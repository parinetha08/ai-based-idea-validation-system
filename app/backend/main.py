from fastapi import FastAPI
from app.backend.routes.validate import router

app = FastAPI()

app.include_router(router)