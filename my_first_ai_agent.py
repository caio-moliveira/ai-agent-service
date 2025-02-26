from langchain.chains import LLMChain
from langchain_aws import ChatBedrock  # ✅ Updated Import
from langchain.prompts import PromptTemplate
import boto3
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    raise ValueError("AWS credentials are missing. Please check your .env file.")

bedrock_client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


llm = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",  # set the foundation model
    model_kwargs={
        "temperature": 0,
        "max_tokens": 1000,
        # "topP": 0.5, # Removido Depreciated
        # "maxTokenCount": 100, # Removido Depreciated
    },
)


def my_chatbot(language, freeform_text):
    prompt = PromptTemplate(
        input_variables=["language", "freeform_text"],
        template="You are a chatbot. You are in {language}.\n\n{freeform_text}",
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt)

    response = bedrock_chain({"language": language, "freeform_text": freeform_text})
    return response


st.title("Bedrock Chatbot")

language = st.sidebar.selectbox("Language", ["english", "spanish"])

if language:
    freeform_text = st.sidebar.text_area(label="What is your question?", max_chars=100)

if freeform_text:
    response = my_chatbot(language, freeform_text)
    st.write(response["text"])
