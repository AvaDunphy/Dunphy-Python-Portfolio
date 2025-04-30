import streamlit as st
import spacy 
from spacy.pipeline import EntityRuler
from spacy import displacy
import pandas as pd
nlp = spacy.load("en_core_web_sm")

import kagglehub
# Download latest version
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

print("Path to dataset files:", path)

#Heading/Small Paragraph/Instructions
st.title("Whats Your Jam? 🎧 ")
st.markdown("""
### Lets simplify finding the perfect song...🎶
BLAH BLAH BLAH BLAH 
What does Tab 1 and Tab 2 provide information about, but not neccessary for the quiz. 
            
**Follow These Steps to Get Started:**
1. Go to the Mood Quiz Tab (Tab 2), and take your quiz. 
2. After being given your mood, go to the Music Recomendation Tab (Tab 3) and input your mood to get your recomendations. 

""")

#Organize the Tabs on the app, different tabs. 
tab1, tab2, tab3, tab4 = st.tabs(["📊Music Data", "📝Take Mood Quiz", "🎶Music Recommendations", "ℹ️About This App"])

# TAB BY TAB BREAK DOWN 

# Tab 1 - Data
with tab1:
    st.title("What are people listening to? 🤷‍♀️")
    st.write(" blah blah blah, heres what the data is, what it shows, what you can do, how it helps")
    # First, inputting the data set into the machine
    csv_path = "/Users/avadunphy/Documents/Dunphy-Python-Portfolio/StreamlitAppFinal/musicdataset.csv"
    df = pd.read_csv(csv_path)

    # Second, making some titles
    st.header("🎵 Spotify Mood Data Preview")
    st.write("Below you will find BLAH BLAH BLAH -- Lets take a look at the first ten rows of the data set:")

    # Third, Let's clean up the data set a little bit
    df_clean = df.drop(columns=['track_id', 'duration_ms', "Unnamed: 0"]) # This line allows me to drop some files that I didn't want showing
    df_clean.columns = df_clean.columns.str.replace('_', ' ', regex=False).str.title() # This makes the titles a little more clean with no "_"
    st.dataframe(df_clean.head(10))

        # 🔍 Filter by genre
    st.subheader("🎼 Filter by Genre")
    
    # Get unique genres (adjust column name if it's not 'Genre')
    genres = df_clean['track_genre'].dropna().unique()
    selected_genre = st.selectbox("Choose a genre to display:", sorted(genres))

    # Filter the DataFrame
    filtered_df = df_clean[df_clean['track_genre'] == selected_genre]

    st.write(f"Showing songs in the **{selected_genre}** genre:")
    st.dataframe(filtered_df.head(10))

# Fourth, let add in some button and interactivty with the audience

# Tab 2 - Quiz
with tab2:
    st.header("📝 Mood Quiz")
    st.write("five questions, lets find out what music you should listen to based on your mood")

# Tab 3 - Recomendations
with tab3:
    st.header("🎵 Music Recommendation ")
    st.write("finally! lets get to the recomendations, what should you listen to. Songs AND artists")

# Tab 4 - About
with tab3:
    st.header(" ℹ️ About")
    st.write("This app was built to help you discover new music based on your mood. Enjoy!")

