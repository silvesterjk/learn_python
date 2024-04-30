from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json 
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

TOKEN = os.environ["TOKEN"]
TOKEN = f"Bearer {TOKEN}"
model1 = os.environ["model1"]
model2 = os.environ["model2"]

class ChatRequest(BaseModel):
    messages: list

@app.post("/chat/")
async def chat(chat_request: ChatRequest):
    url = "https://api.together.xyz/v1/chat/completions"

    payload = {
        "model": model1,
        "stop": ["<|im_end|>", "<|im_start|>", "<|eot_id|>"],
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "messages": chat_request.messages,
        "temperature": 0.7,
        "top_p": 0.7,
        "repetition_penalty": 1,
        "top_k": 50
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": TOKEN
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {"content": data['choices'][0]['message']['content']}
    else:
        raise HTTPException(status_code=400, detail="Error processing request")
    
@app.post("/grammar/")
async def grammar(chat_request: ChatRequest):
    url = "https://api.together.xyz/v1/chat/completions"

    payload = {
        "model": model2,
        "stop": ["<|im_end|>", "<|im_start|>"],
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "messages": chat_request.messages,
        "temperature": 0.0,
        "top_p": 0.7,
        "repetition_penalty": 1,
        "top_k": 50
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": TOKEN
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {"content": data['choices'][0]['message']['content']}
    else:
        raise HTTPException(status_code=400, detail="Error processing request")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


