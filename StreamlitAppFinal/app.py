import streamlit as st
import spacy 
from spacy.pipeline import EntityRuler
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

import kagglehub

# Download latest version
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

print("Path to dataset files:", path)