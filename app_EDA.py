# import the required libraries

import os
from api_key import apikey

import streamlit as st
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

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