#import streamlit as st
#from scripts.translate import translate

import streamlit as st
#from scripts.fefe_translator import FefeTranslator

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.translate import translate


st.title("Fe'efe'e AI Translator")

text=st.text_input("Enter sentence")

if st.button("Translate"):

    result=translate(text)

    st.write(result)
