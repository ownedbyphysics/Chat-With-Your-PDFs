from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

openai_api_key = ''

def get_conversation_chain(db):
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm( 
    llm=llm,
    retriever = db.as_retriever(),
    memory = memory
    )

    return conversation_chain