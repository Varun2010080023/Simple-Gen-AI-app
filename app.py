import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = "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"

os.environ["LANGCHAIN_TRACING_V2"]="true"
langchain_project = os.getenv("LANGCHAIN_PROJECT")
if langchain_project is not None:
    os.environ["LANGCHAIN_PROJECT"] = langchain_project
else:
    # You can either assign a default or raise an error/warning
    os.environ["LANGCHAIN_PROJECT"] = "default_project_name"  # or just skip setting it
    print("Warning: LANGCHAIN_PROJECT environment variable not set.")


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


