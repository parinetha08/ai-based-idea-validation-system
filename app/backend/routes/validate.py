from fastapi import APIRouter

router = APIRouter()

@router.post("/validate")
def validate():
    return {"message": "working"}