import streamlit as st
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import os
import getpass

from dotenv import load_dotenv
load_dotenv()
docs = WebBaseLoader("https://jamesclear.com/five-step-creative-process").load()
splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever=vectorstore.as_retriever()

prompt = hub.pull("rlm/rag-prompt")



groq_api_key=os.environ['GROQ_API_KEY']
#groq_api_key="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"
#llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, chain)

response = rag_chain.invoke({"input": "What is creative process of AI?"})
print(response["answer"])







