## Integrate our module with OpenAI API 

import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework

st.title("OpenAI LangChain Demo")
input_text = st.text_input("Enter your text here")


llm = OpenAI(temperature=0.5)

if input_text:
    st.write(llm(input_text))



