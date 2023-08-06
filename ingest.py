import os

from langchain.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
)
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

ABS_PATH: str = os.path.dirname(os.path.abspath(__file__))
DB_DIR: str = os.path.join(ABS_PATH, "db")


# Create vector database
def create_vector_database():
    """
    Creates a vector database using document loaders and embeddings.

    This function loads data from PDF, markdown and text files in the 'data/' directory,
    splits the loaded documents into chunks, transforms them into embeddings using HuggingFace,
    and finally persists the embeddings into a Chroma vector database.

    """
    # Initialize loaders for different file types
    pdf_loader = DirectoryLoader("data/", glob="**/*.pdf", loader_cls=PyPDFLoader)
    markdown_loader = DirectoryLoader(
        "data/", glob="**/*.md", loader_cls=UnstructuredMarkdownLoader
    )
    text_loader = DirectoryLoader("data/", glob="**/*.txt", loader_cls=TextLoader)

    all_loaders = [pdf_loader, markdown_loader, text_loader]

    # Load documents from all loaders
    loaded_documents = []
    for loader in all_loaders:
        loaded_documents.extend(loader.load())

    # Split loaded documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=40)
    chunked_documents = text_splitter.split_documents(loaded_documents)

    # Initialize HuggingFace embeddings
    huggingface_embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )

    # Create and persist a Chroma vector database from the chunked documents
    vector_database = Chroma.from_documents(
        documents=chunked_documents,
        embedding=huggingface_embeddings,
        persist_directory=DB_DIR,
    )

    vector_database.persist()


if __name__ == "__main__":
    create_vector_database()
