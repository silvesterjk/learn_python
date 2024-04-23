import requests
import json

lang_memory = [[
    {
      "role": "user",
      "content": "Hello"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I help you today? Is there anything you would like to talk about or ask me a question about? I'm here to assist you with any information or advice you might need."
    },
    {
      "role": "user",
      "content": "Hello"
    }
  ],
  
  "stop": [
    "<|endoftext|>",
    "<|im_end|>"
  ]]

messages = lang_memory

url = "https://api.fireworks.ai/inference/v1/chat/completions"
payload = {
  "model": "accounts/fireworks/models/qwen-14b-chat",
  "max_tokens": 1024,
  "top_p": 1,
  "top_k": 40,
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "temperature": 0.6,
  "messages": messages
}
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "Bearer <API_KEY>"
}
requests.request("POST", url, headers=headers, data=json.dumps(payload))