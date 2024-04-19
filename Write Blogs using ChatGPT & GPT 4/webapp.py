
### login to openai

import os
from dotenv import load_dotenv
load_dotenv('.env')

from openai import OpenAI
OPENAI_API_KEY = os.environ.get("key")
client = OpenAI(api_key=OPENAI_API_KEY)


import streamlit as st
st.image("snipped.PNG")

st.title("AI Content Creator by We4AI")
st.markdown("### Built with :heart: using Python & OpenAI models")

# Input options
model_name = st.selectbox("Select Model", ["gpt-3.5-turbo-0125", "gpt-3.5-turbo", "gpt-4-turbo"])
system = st.text_area("Select System behaviour", 
                      value="You are an SEO expert and content writer. Your objective is to bring more viewers for the content that you write for your company")
task = st.text_area("Enter the blog topic and briefly mention details", value="Input details about the blogpost")



# Submit button
if st.button("Submit"):
    completion = client.chat.completions.create(
    model= model_name,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", 
        "content": task+"\n output the text in markdown with proper formatting"}
    ]
    )
    
    st.markdown(completion.choices[0].message.content)
