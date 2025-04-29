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

st.markdown("""
### Lets simplify finding the perfect song...🎶
# BLAH BLAH BLAH BLAH 

""")

import streamlit as st

st.title("🎶 Mood-Based Music Recommender 🎶")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Take Mood Quiz", "Music Recommendations", "About This App"])

# Tab 1 - Quiz
with tab1:
    st.header("📝 Mood Quiz")
    st.write("This is where your quiz questions go!")

# Tab 2 - Recommendations
with tab2:
    st.header("🎵 Music Recommendations")
    st.write("After you find your mood, your music suggestions will show up here!")

# Tab 3 - About
with tab3:
    st.header("ℹ️ About")
    st.write("This app was built to help you discover new music based on your mood. Enjoy!")

