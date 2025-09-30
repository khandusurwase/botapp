import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()  # read .env file

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3,
    max_tokens= 700,
    api_key=openai_api_key

)
llm
key = openai_api_key

embedding = OpenAIEmbeddings(api_key=openai_api_key)