import streamlit as st
import spacy 
from spacy.pipeline import EntityRuler
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

## Import Spotify Tracks Dataset 
import kagglehub

# Download latest version
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

st.title("Whats Your Jam?")
