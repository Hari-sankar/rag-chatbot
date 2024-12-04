# from fastapi import APIRouter
# from fastapi.responses import StreamingResponse
# from app.services.chat_service import get_openai_generator

# router = APIRouter()

# # Stream Chat Completion API
# @router.get("")
# async def stream(prompt: str):
#     return StreamingResponse(get_openai_generator(prompt), media_type='text/event-stream')
