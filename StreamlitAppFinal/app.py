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

BLAH BLAH BLAH BLAH 

## Follow These Steps to Get Started:
1. Look at the data! Take a look at the different kind of music offered, and how it relates to different generes.
2. Take your quiz! 
3. In put your mood into music recommendations and find what songs are best for you now. 

""")


# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Song Data", "Take Mood Quiz", "Music Recommendations", "About This App"])

# Tab 1 - Data
with tab1:
    st.header("Song Data")
    st.write("DATA")

# Tab 2 - Quiz
with tab2:
    st.header("📝 Mood Quiz")
    st.write("Quiz")

# Tab 3 - Recomendations
with tab3:
    st.header("🎵 Music Recommendation ")
    st.write("Recs")

# Tab 4 - About
with tab3:
    st.header(" ℹ️ About")
    st.write("This app was built to help you discover new music based on your mood. Enjoy!")

   

