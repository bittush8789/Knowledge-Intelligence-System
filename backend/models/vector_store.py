from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os

class VectorStore:
    def __init__(self, path):
        self.embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.vector_store = Chroma(
            persist_directory=path,
            embedding_function=self.embeddings
        )

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
        self.vector_store.persist()

    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)
