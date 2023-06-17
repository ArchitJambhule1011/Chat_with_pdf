from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_base(chunks):
    embeddings = OpenAIEmbeddings()
    vector_base = FAISS.from_texts(chunks, embeddings)
    return vector_base