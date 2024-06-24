import os
from typing import Annotated
from fastapi import HTTPException, Header
from openai import OpenAI
import anthropic
import google.generativeai as genai

#Google Gemini AI
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1000,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
chat_session = model.start_chat(
  history=[
  ]
)

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

#Open AI
openai_client = OpenAI()

#Anthropic AI
anthropic_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))