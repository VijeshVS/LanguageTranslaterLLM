import streamlit as st
from deep_translator import GoogleTranslator as Translator
from gtts import gTTS
import os


language_dict = {
    'english': 'en',
    'spanish': 'es',
    'french': 'fr',
    'german': 'de',
    'chinese': 'zh',
    'hindi': 'hi',
    'arabic': 'ar',
    'japanese': 'ja',
    'russian': 'ru',
    'korean': 'ko',
    'portuguese': 'pt',
    'italian': 'it',
    'dutch': 'nl',
    'greek': 'el',
    'turkish': 'tr',
    'swedish': 'sv',
    'norwegian': 'no',
    'danish': 'da',
    'finnish': 'fi',
    'polish': 'pl',
    'hungarian': 'hu',
    'czech': 'cs',
    'romanian': 'ro',
    'thai': 'th',
    'vietnamese': 'vi',
    'indonesian': 'id',
    'malay': 'ms',
    'hebrew': 'he',
    'persian': 'fa',
    'bengali': 'bn',
    'urdu': 'ur',
    'swahili': 'sw',
    'filipino': 'fil',
    'ukrainian': 'uk',
    'bulgarian': 'bg',
    'croatian': 'hr',
    'serbian': 'sr',
    'slovak': 'sk',
    'slovenian': 'sl',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'estonian': 'et',
    'icelandic': 'is',
    'irish': 'ga',
    'welsh': 'cy',
    'scots_gaelic': 'gd',
    'basque': 'eu',
    'catalan': 'ca',
    'galician': 'gl',
    'albanian': 'sq',
    'bosnian': 'bs',
    'macedonian': 'mk',
    'armenian': 'hy',
    'georgian': 'ka',
    'azerbaijani': 'az',
    'kazakh': 'kk',
    'gujarati':'gu',
    'uzbek': 'uz',
    'mongolian': 'mn',
    'tamil': 'ta',
    'telugu': 'te',
    'kannada': 'kn',
    'malayalam': 'ml',
    'sinhala': 'si',
    'nepali': 'ne',
    'burmese': 'my',
    'khmer': 'km',
    'lao': 'lo',
    'tibetan': 'bo',
    'somali': 'so',
    'hausa': 'ha',
    'igbo': 'ig',
    'yoruba': 'yo',
    'zulu': 'zu',
    'xhosa': 'xh',
    'sesotho': 'st',
    'shona': 'sn',
    'tswana': 'tn',
    'chichewa': 'ny',
    'tigrinya': 'ti',
    'amharic': 'am',
}

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=language_dict.get(lang))
    tts.save("output.mp3")

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
        text_to_speech(translated, text_input)
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

chatbot()