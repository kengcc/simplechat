
#langchain dependencies
from langchain_openai import ChatOpenAI    # LLM Model
from langchain_core.prompts import ChatPromptTemplate # Prompt Input
from langchain_core.output_parsers import StrOutputParser # Output Display


# interface
import streamlit as st  # User Interface

#environment variables
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistance. Please respond to user queries."),
        ("user", "Question:{question}")
    ]
)

## Streamlit Framework
st.title('Langchain Demo with OpenAI')
input_text=st.text_input("Search the topic you want.")

#OpenAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
