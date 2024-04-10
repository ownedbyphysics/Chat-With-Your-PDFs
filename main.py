import time
import streamlit as st 
from dotenv import load_dotenv
from processText import extractPdfText, textChunks, vectorDB
from chatWithPDF import get_conversation_chain
from templates import css, bot_template, user_template



def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']  
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    #load_dotenv()
    
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
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if 'user_question' not in st.session_state:
        st.session_state.user_question = None
    st.title('Ask your PDFs :books: ')
    
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
   
    
    def submit():
        st.session_state.user_question = st.session_state.widget
        st.session_state.widget = ''
    
    user_question = st.text_input("Ask a question about your documents:",
                                   key='widget', on_change=submit)
    
    if st.session_state.user_question:
        handle_userinput(st.session_state.user_question)
    else: print('no question yet')
    
    with st.sidebar:
        st.subheader('Your docs go here:')
        pdfs = st.file_uploader("Import here your pdfs: :pushpin:", accept_multiple_files=True)
        if st.button('Feed me!'):
            with st.spinner('Processing'):
                text = extractPdfText(pdfs)
                chunks = textChunks(text)
                embeddingsDB = vectorDB(chunks)
                st.session_state.conversation = get_conversation_chain(embeddingsDB)
            st.write("Done!")
            time.sleep(5) 
            
                
                #st.write(embeddingsDB)





if __name__ == "__main__":
    main()