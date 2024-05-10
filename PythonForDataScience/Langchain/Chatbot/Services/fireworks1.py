from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_fireworks import ChatFireworks
import json
import os

FIREWORKS_API_KEY = ""

if "FIREWORKS_API_KEY" not in os.environ:
    os.environ["FIREWORKS_API_KEY"] = FIREWORKS_API_KEY

chat = ChatFireworks(model="accounts/fireworks/models/llama-v3-8b-instruct",
                    temperature=0.7,
                    max_tokens=40)

system_message = SystemMessage(content="You are a Human Resource Manager working for Talking Yak Corporation. You are in middle of interviewing a candidate who is applied for the junior developer position in the frontend team. \n. Follow the given instructions: \n 1. You always respond back in 20 words. 2. You will first acknowledge the user response and then continue the conversation by asking another question")
ai_message = AIMessage(content="Hello! I am Cynthia. I work as a Human resource Manager at Talking Yak. Nice to meet you. Tell me about yourself.")
human_message = HumanMessage(content="My name is Nicy and I have applied for the junior developer role. I like coding. I developed the front end for an e-commerce platform")

response = chat.invoke([system_message, human_message])
text = response.content
json_text = json.dumps({'content': text})
print(json_text)