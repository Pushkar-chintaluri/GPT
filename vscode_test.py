import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

open_ai_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=open_ai_key)
    st.info(llm(input_text))

with st.form('my form'):
    text = st.text_area('Enter text:','What are the three key pieces of advice for learning how to code?' )
    submitted = st.form_submit_button('Submit')
    if not open_ai_key.startswith('sk-'):
        st.warning('API Key Invalid!', icon='⚠')
    if submitted and open_ai_key.startswith('sk-'):
        generate_response(text)
