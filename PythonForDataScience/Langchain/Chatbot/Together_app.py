from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# ## Langmith tracking
# os.environ["TOGETHER_KEY"] = TOGETHER_KEY
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=LANGCHAIN_API_KEY
TOGETHER_KEY = ""

## Prompt Template

messages = [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]

prompt=ChatPromptTemplate.from_messages(
    messages
)

# openAI LLm 
llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=0,
    max_tokens=128,
    top_k=1,
    together_api_key= TOGETHER_KEY
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

question = "What is your name?"
print(chain.invoke({'question':question}))