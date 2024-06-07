RAG system to retrieve information of your pdfs. 
It can operate with 2 different modes. 

Single shot: In this mode the user uploads one or more pdfs and asks questions about them.
It is a single shot because once the program is closed the information (embeddings) are not stored anywhere
and the user has to re-upload the documents to re-use them.

Storage: The storage mode provides you the ability to create your own database of pdfs and save them locally.
The load option later asks you to provide the name of the dataset to load it (load the stored embeddings) and start asking questions.

How to use:
1. clone the repo
2. make sure to install the dependencies stated in the requirements.txt file
3. make sure to use your own open_ai key. You can create one here -> https://platform.openai.com/api-keys
4. open a command prompt, navigate to the directory you cloned the project and run the following command 'streamlit run main.py'


   Page screenshot:
   ![image](https://github.com/ownedbyphysics/Chat-With-Your-PDFs/assets/48797734/83c15889-ac09-4feb-8a50-86fa8bc9f63f)
