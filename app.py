import streamlit as st
from deep_translator import GoogleTranslator as Translator

def chatbot():
    st.title("Language Translator")
    user_input = st.text_input("Text to be translated", "")
    text_input = st.text_input("Translate to ?", "")
    button_input = st.button("Translate")
    try:
        translated = Translator(source='auto', target=text_input).translate(user_input)
    except Exception as e:
        translated = "Please enter valid inputs"
    
    if button_input:
        st.text_area("Generated response", value=translated ,height=200, key="generated_response", disabled=True)

chatbot()