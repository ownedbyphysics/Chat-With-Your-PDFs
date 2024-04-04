import streamlit as st 
from dotenv import load_dotenv
from processText import extractPdfText, textChunks, vectorDB
from chatWithPDF import get_conversation_chain
from templates import css, bot_template, user_template



def handle_userinput(user_question):
    response = st.session_state.chat({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    
    st.set_page_config(page_title='Ask Your PDFs:', 
                       page_icon=":books:",
                       layout="wide",
                       initial_sidebar_state="expanded",
                    )  
    
    st.write(css, unsafe_allow_html=True)
    
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
        </style>
        """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.chat = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.title('Ask your PDFs :books: ')
    #st.text_input('Ask a question')
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)
    else: print('lalala')
    
    with st.sidebar:
        st.subheader('Your docs go here:')
        pdfs = st.file_uploader("Import here your pdfs: :pushpin:", accept_multiple_files=True)
        if st.button('Feed me!'):
            with st.spinner('Processing'):
                text = extractPdfText(pdfs)
                chunks = textChunks(text)
                embeddingsDB = vectorDB(chunks)
                st.session_state.chat = get_conversation_chain(embeddingsDB)
                
                #st.write(embeddingsDB)





if __name__ == "__main__":
    main()