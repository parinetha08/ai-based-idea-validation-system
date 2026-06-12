from fastapi import FastAPI
from app.backend.routes.validate import router

app = FastAPI(title="AI Idea Validator")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "AI Idea Validator API Running"}
