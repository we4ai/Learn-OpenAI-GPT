import os
from dotenv import load_dotenv
load_dotenv('.env')

openai_key = os.environ.get('key')
from openai import OpenAI
client = OpenAI(api_key = openai_key)



import streamlit as st
st.image("snipped.PNG")

st.title("AI Content Generator by We4AI")


### Input options
# 1. Model selection
model_name = st.selectbox("Select the Model",
             ['gpt-4-turbo', 'gpt-3.5-turbo-0125', 'gpt-3.5-turbo'])


sys_content = """
You are an SEO expert and content writer.
Your objective is to bring more viewers for the content you write for your company.
"""

system = st.text_area("Enter the System Behaviour", 
                      value=sys_content)

task = st.text_area("Enter the blog post topic and briefly mention about it.", 
                    value = "Input details about the blog post")


if st.button("Submit"):
    completion = client.chat.completions.create(
    model = model_name,
    messages = [
        {'role': "system", 'content': system},
        {'role': "user", 'content': task+" Please output everything with proper formatting in markdown"},
    ],
    seed= 100
    )
    
    st.markdown(completion.choices[0].message.content)
    
    
    