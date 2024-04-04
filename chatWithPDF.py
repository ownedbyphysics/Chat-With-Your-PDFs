from langchain.memory import ConversationBufferMemory
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain


def get_conversation_chain(db):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm( 
    llm=llm,
    retriever = db.as_retriever(),
    memory = memory
    )

    return conversation_chain