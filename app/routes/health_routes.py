from fastapi import APIRouter, HTTPException
from app.db.session import get_db
from app.models.response import BaseResponse, format_response

router = APIRouter()

# Health API
@router.get(
    "", 
    response_model=BaseResponse, 
    responses={
        200: {"model": BaseResponse, "description": "Health check succeeded"},
        400: {"model": BaseResponse, "description": "Health check failed - Database Connection Failed"},
        500: {"model": BaseResponse, "description": "Internal Server Error"}
    }
)
def health_check():
    try:
        with get_db() as db:
            db.execute("SELECT 1")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Health Check - DataBase Connection Failed")
    return format_response(200, "Health Check - Success")
