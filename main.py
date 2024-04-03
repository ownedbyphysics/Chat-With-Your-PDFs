import streamlit as st 
from dotenv import load_dotenv
from extractText import extractPdfText

def main():
    load_dotenv()
    
    st.set_page_config(page_title='Ask Your PDFs:', 
                       page_icon=":books:",
                       layout="wide",
                       initial_sidebar_state="expanded",
                    )  
    
    
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
    
    st.title('Ask your PDFs :books: ')
    st.text_input('Ask a question')
    
    with st.sidebar:
        st.subheader('your docs')
        pdfs = st.file_uploader("Import here your pdfs: :pushpin:", accept_multiple_files=True)
        if st.button('Feed me!'):
            with st.spinner('Processing'):
                text = extractPdfText(pdfs)
                st.write(text)





if __name__ == "__main__":
    main()