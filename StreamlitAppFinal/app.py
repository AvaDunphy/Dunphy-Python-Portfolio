import streamlit as st
import spacy 
from spacy.pipeline import EntityRuler
from spacy import displacy


nlp = spacy.load("en_core_web_sm")

## Import Spotify Tracks Dataset 
import kagglehub

# Download latest version
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

st.title("Whats Your Jam? 🎧 ")

st.markdown(""
            Hey There! Do you struggle to find the perfect song to fit the mood? Wether you trying to study, cook, 
            chill out, or get hype. Well look no further! blah blah blah blah blah
            "")
