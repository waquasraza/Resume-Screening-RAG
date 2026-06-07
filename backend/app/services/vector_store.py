from langchain_chroma import Chroma
from app.services.embeddings import get_embeddings


def store_resume_chunks(chunks):
    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_store