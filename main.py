import time
import streamlit as st 
from dotenv import load_dotenv
from processText import extractPdfText, textChunks, vectorDB
from chatWithPDF import get_conversation_chain
from templates import css, bot_template, user_template




def handle_userinput(user_question):
    if st.session_state.conversation is not None:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']  
        
        for i, message in enumerate(st.session_state.chat_history):
            print(st.session_state.chat_history)
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
                
                st.markdown("---")
    else: print('clear chat')

def main():
    #load_dotenv()
    
    st.set_page_config(page_title='Ask Your PDFs:', 
                       page_icon=":books:",
                       layout="wide",
                       initial_sidebar_state="expanded",
                    )  
    st.image("cover2.jpg", use_column_width=False, width=500) 
   
   
   
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
    
    
    def reset_conversation():
        st.session_state.conversation = None
        st.session_state.chat_history = None
        #st.session_state.user_question = None
    st.button('Reset Chat', on_click=reset_conversation, key='reset_chat')
    
    with st.sidebar:
        
        st.markdown(
            """
            <style>
                section[data-testid="stSidebar"] {
                    width: 300px !important; # Set the width to your desired value
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        option = st.radio("Choose an option:", ("Load", "Create"), index=None, key='mode_radio' )
        
        if not option: 
            st.write('')
        elif option == "Create": 
            create_option = st.radio("Choose an option:", ("Storage", "Single Shot"), index=None, key="create_radio")
            if not create_option: 
                st.write('choose among single shot, or build your own database of pdf info')
            elif create_option == 'Single Shot':
                
                
                
                st.subheader('Your docs go here:')
                pdfs = st.file_uploader("Import here your pdfs: :pushpin:", accept_multiple_files=True, type='pdf')
                if st.button('Feed me!'):
                        with st.spinner('Processing'):
                            text = extractPdfText(pdfs)
                            chunks = textChunks(text, True)
                            embeddingsDB = vectorDB(chunks)
                            st.session_state.conversation = get_conversation_chain(embeddingsDB)
                        st.write("Done!")
                        time.sleep(5) 
            else:
                db_name = st.text_input("Give a name for the database:")
                if db_name:
                    st.subheader('Your docs go here:')
                    pdfs = st.file_uploader("Import here to start building your database: :pushpin:", accept_multiple_files=True, type='pdf')
                    if st.button('Feed me!'):
                        with st.spinner('Processing'):
                            text = extractPdfText(pdfs)
                            chunks = textChunks(text, False)
                            embeddingsDB = vectorDB(chunks)
                            model = get_conversation_chain(embeddingsDB)
                            
                            st.write(model({'question': 'What is Spyros job'}))
                            time.sleep(5)
        else:
        
            st.write('implement load')
                    
      





if __name__ == "__main__":
    main()