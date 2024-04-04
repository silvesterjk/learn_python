from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv



## Langmith tracking
os.environ["TOGETHER_KEY"] = TOGETHER_KEY
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=LANGCHAIN_API_KEY

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# ## Langmith tracking
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo')
input_text=st.text_input("Enter your text here:")

# openAI LLm 
llm = Together(
    model="upstage/SOLAR-10.7B-Instruct-v1.0",
    temperature=0,
    max_tokens=128,
    top_k=1,
    together_api_key= TOGETHER_KEY
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))