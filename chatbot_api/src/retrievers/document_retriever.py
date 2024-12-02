import dotenv
import logging
import os

from embeddings.custom_embeddings import MyEmbeddingFunction

from langchain_community.vectorstores.chroma import Chroma

dotenv.load_dotenv()

CHROMA_HOST = os.getenv("CHROMA_HOST")
CHROMA_PORT = os.getenv("CHROMA_PORT")
CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME")
CHROMA_DATA_DIR = os.getenv("CHROMA_DATA_DIR")

DOCUMENT_PATH = os.getenv("DOCUMENT_PATH")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

LOGGER = logging.getLogger(__name__)

embeddings = MyEmbeddingFunction()

db = Chroma(
    collection_name=CHROMA_COLLECTION_NAME,
    persist_directory=CHROMA_DATA_DIR,
    embedding_function=embeddings
)

retriever = db.as_retriever()