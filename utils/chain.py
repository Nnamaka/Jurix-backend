from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from .openai_vars import llm_name
from .vector_db import vectordb

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

llm = ChatOpenAI(model_name=llm_name, temperature=0)

retriever = vectordb.as_retriever()
qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=retriever,
    memory=memory
)