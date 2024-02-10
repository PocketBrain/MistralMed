from langchain.embeddings import LlamaCppEmbeddings
from langchain.llms import LlamaCpp
from settings import ModelSettings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import  FAISS


class Model:
    def __init__(self):
        self.model = LlamaCpp(
        model_path=ModelSettings.PATH,
        n_gpu_layers=-1,
        temperature=0.2,
        top_p=1,
        verbose=True,
        n_ctx=4096
    )

class Embeddings:
    def __init__(self):
        self.embeddings = LlamaCppEmbeddings(model_path=ModelSettings.PATH)
        self.loader = TextLoader(ModelSettings.PATH_DATA)

    def splitDocs(self):
        docs = self.loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
        text_chunks = text_splitter.split_documents(docs)
        return text_chunks

    def createEmbeddings(self):
        text_chunks = self.splitDocs()
        db = FAISS.from_documents(text_chunks, self.embeddings)
        db.save_local('faiss_index')
        return db
