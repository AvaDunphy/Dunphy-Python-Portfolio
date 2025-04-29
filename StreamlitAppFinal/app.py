import streamlit as st
import spacy 
from spacy.pipeline import EntityRuler
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

## Import Spotify Tracks Dataset 
import kagglehub

# Download latest version
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

print("Path to dataset files:", path)

nlp = spacy.load("en_core_web_sm")

st.title("Named Entity Recognition (NER) App ")

st.markdown("""
### 🙋‍♀️ Hello NER Explorer! 

Are you interested in uncovering the grammar and patterns in passages, texts, and books?  
Do you struggle to understand patterns within complicated texts? Well, look no further!  

This Named Entity Recognition App breaks down sentence structures, illuminating different words or phrases that are important to you and your text.  

**What to do:**
1. Write your own text in the text box **or** upload a `.txt` file.
2. Specify the custom **label** and **pattern** you are looking for.
3. Click **Run NER** to highlight entities instantly!
            

⬇️ Now lets get started!
""")
