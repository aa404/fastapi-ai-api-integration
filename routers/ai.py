from fastapi import APIRouter
from ..dependencies import openai_client, anthropic_client, chat_session

router = APIRouter()

@router.post("/openai", tags=["openAI"])
def ask_chatgpt(message: str):
    response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
       {"role": "user", "content": message},
    ]
    )
    return response.choices[0].message

@router.post("/gemini", tags=["gemini"])
def ask_gemini(message: str):
    response = chat_session.send_message(message)
    return response.text

@router.post("/claude", tags=["claude"])
def ask_claude(message: str):
    response = anthropic_client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=500,
    messages=[
        {"role": "user", "content": message}
    ]
    )
    return response.content