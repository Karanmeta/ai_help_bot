from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_vectorstore_retriever():
    documents = [
        "The INSAT-3D satellite, managed by ISRO, provides rainfall estimates for the Indian subcontinent.",
        "The Rainfall Product, also known as Rainfall Estimate, is derived from the INSAT-3D satellite and is updated every 15 minutes.",
        "Cloud mask products help in identifying cloud-free regions for various applications and are derived from INSAT-3D.",
        "ISRO is the primary space agency of India and manages many satellite missions.",
    ]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.create_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore.as_retriever()