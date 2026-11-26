import streamlit as st
from models import gemini


st.title('Streamlit :blue[pro]:red[project] :grin:',icon='💀')

st.title('Streamlit :blue[pro]:red[project] :grin:',icon='💀')

st.header('Gemini Project :green[:robot]')

st.subheader('Using Gemini-3.6-flash Model')

# st.txt_input('prompt')

prompt = st.text_area('Enter your prompt',
                     placeholder='explain about anamil')
button_click = st.button('Send Prompt :aeroplane:')  
if button_click:
    if prompt.strip()=='':
        st.warning('Prompt field cannot be empty.')
    else:
        with st.spinner('Generating content...'):
            answer = gemini(prompt)
            st.success('Content generated.')   
            st.write (answer)