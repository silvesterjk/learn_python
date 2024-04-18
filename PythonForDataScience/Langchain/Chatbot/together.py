 #%%

import requests

messages = [
        {
            "content": "Hello there",
            "role": "user"
        },
        {
            "content": "What are you up to?",
            "role": "user"
        }
    ]


endpoint = 'https://api.together.xyz/v1/chat/completions'

res = requests.post(endpoint, json={
    "model": "Qwen/Qwen1.5-14B-Chat",
    "max_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1,
    "stop": [
        "<|im_end|>",
        "<|im_start|>"
    ],
    "messages": messages
}, headers={
    "Authorization": "Bearer cc73c0e5c4a10bb916926eb3c614974af2414bf997b0e9bd8a92544a97d1b79e",
})
# %%
from openai import OpenAI

#import os

messages = [
    {
      "role": "system",
      "content": "You are a helpful assistant. You give responses in under 50 words at all times.",
    },
    {
      "role": "user",
      "content": "What are the planets in Solar System",
    }
  ]

TOGETHER_API_KEY = "cc73c0e5c4a10bb916926eb3c614974af2414bf997b0e9bd8a92544a97d1b79e"

client = OpenAI(
  api_key=TOGETHER_API_KEY,
  base_url='https://api.together.xyz/v1',
)

chat_completion = client.chat.completions.create(
  messages= messages,
  model="Qwen/Qwen1.5-7B-Chat",
  temperature = 0.7,
)

print(chat_completion.choices[0].message.content)
# %%

from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_together import Together

template = """You are a chatbot having a conversation with a human.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

TOGETHER_API_KEY = "cc73c0e5c4a10bb916926eb3c614974af2414bf997b0e9bd8a92544a97d1b79e"

llm = Together(
    model="Qwen/Qwen1.5-7B-Chat",
    temperature=0.7,
    max_tokens=128,
    top_k=1,
    together_api_key= TOGETHER_API_KEY
)
# llm = "Qwen/Qwen1.5-7B-Chat"
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory,
)

llm_chain.predict(human_input="Hi there my friend")
# %%
