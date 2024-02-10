from model import Model, Embeddings
from langchain.chains import RetrievalQA
from settings import ModelSettings


llm = Model.model()
db = Embeddings.createEmbeddings()
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())

while True:
    query = input("Введите запрос")
    qa.invoke(ModelSettings.SYSTEM_PROMPT + query)