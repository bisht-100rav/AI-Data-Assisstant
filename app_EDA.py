# import the required libraries

import os
from api_key import apikey

import streamlit as st
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv
import time
import threading

#OpenAI key
os.environ['OPENAI_API_KEY']= apikey
load_dotenv(find_dotenv())

# lll model
llm = OpenAI()

# Rate limiter configuration
RATE_LIMIT_DELAY = 1  # Delay between consecutive API calls in seconds
lock = threading.Lock()

# Main

st.title('AI Assisstant for Data Science')
st.header('Exploratory Data Analysis')
st.subheader('Solution')
st.write('Hello, I am you AI Assisstant and I am here to help you with your data science projects')

with st.sidebar:
    st.write('*Your Data Science adventure begins with the CSV file.*')
    st.caption('''**You may already know that every data science journey starts with a dataset. 
    That's why I'd love for you to upload a csv file.
    Once we have yout data in hand, we'll dive into the understanding it and have some exploring it.
    Then, we will worl together to shape your business challenge into a data science framework. I'll introduce you to the coolest machine learning models, and we will use them to tackle your problem.
    Sounds fun right.**''')

    # was not able to import divier use markdown instead
    # st.divider()


    st.markdown('---')

    st.caption("<p style='text-align:center'> made by Saurav Bisht </p>", unsafe_allow_html=True)

# Initialize the key
if 'clicked' not in st.session_state:
    st.session_state.clicked= {1:False}

# Function to update the value in the session state
def clicked(button):
    st.session_state.clicked[button] = True

# Rate limit 
def get_response(query):
    with lock:
        time.sleep(RATE_LIMIT_DELAY)
        return llm(query)

st.button("Let's get started", on_click = clicked, args=[1])
if st.session_state.clicked[1]:
    st.header('Exploratory Data Analysis Part')
    st.subheader('Solution')

    # csv file uploader
    user_csv = st.file_uploader("Upload yout file heare", type='csv')

    if user_csv is not None:
        user_csv.seek(0)
        df= pd.read_csv(user_csv, low_memory = False)

with st.sidebar:
    with st.expander('What are the steps of EDA'):
            st.write(get_response('What are the steps of EDA'))