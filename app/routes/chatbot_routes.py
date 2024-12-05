from fastapi import APIRouter, File, UploadFile
from app.models.chat import ChatInput
from app.models.response import format_response
from app.services import chatbot_services


router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        return await chatbot_services.process_document(file)
    except Exception as e:
        raise format_response(code = 500,message=str(e))
    

@router.post("/chat")
async def chat(chat_input: ChatInput):
    try:
        return await chatbot_services.get_chat_response(chat_input.question)
    except Exception as e:
        raise format_response(code = 500,message=str(e))
    
