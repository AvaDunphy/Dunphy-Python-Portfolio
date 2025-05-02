import streamlit as st
import spacy 
from spacy.pipeline import EntityRuler
from spacy import displacy
import pandas as pd
from PIL import Image
nlp = spacy.load("en_core_web_sm")

import kagglehub
# Download latest version
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

print("Path to dataset files:", path)

#Heading/Small Paragraph/Instructions
st.title(" Whats Your Jam? 🎧 ")

st.subheader(" Lets simplify finding the perfect song...🎶")
st.markdown("""
Have you ever been caught, unsure of what to put on the radio? Wether you want to listen to some slow jazz, 
some up beat pop, maybe rap? Well, look no further! In this app, you are able to either take a peak 
at what others are listening to OR get recommendations based on your mood. As you can see from below, there
is a data set filled with different songs, artists, genres, etc, that will provide some inspiration, but if thats
not enough, scroll over to the second tab to take a mood quiz. From there, take your mood to the recommendations tab 
and find what songs go best with your mood! 

""")           

st.subheader(" **It's Simple! Follow These Steps to Get Started:** 🪜")
st.markdown("""

1️⃣ Do a little research below, find some inspiration in our data.

2️⃣ Take your mood quiz on tab 2! 

3️⃣ Then insert your mood into tab 3 and get fast reliable recommendations! 
""")

#Organize the Tabs on the app, different tabs. 
tab1, tab2, tab3, tab4 = st.tabs(["📊 Music Data", "📝 Take Mood Quiz", "🎶 Music Recommendations", "ℹ️ About This App"])

# TAB BY TAB BREAK DOWN 

# Tab 1 - Data Table For Research 
with tab1:
    st.header("Let's Look At The Data 👨‍💻")
    st.subheader("What are people listening to? 🤷‍♀️")
    st.write(" With millions of songs out there, it is almost impossible to try and figure out what to listen to. " \
    "So, let me help you out a little! Below find a data set with thousands of the most popular songs on Spotify. This way if you are unsure what you want to play, " \
    "you can just look below! Also, if you are trying to find a specific artist, genre, song, tempo, or popularity, use the filter " \
    "program to zone in on your search. While looking, please keep in mind that there are so so many songs out in the world, and this data set might not have everything, " \
    "BUT it can sure give you a good idea of what you can listen to." \
    "Thank you! And sit back, relax, and enjoy some good music 🫶🏻")

    # First, inputting the data set into the machine
    csv_path = "/Users/avadunphy/Documents/Dunphy-Python-Portfolio/StreamlitAppFinal/musicdataset.csv"
    df = pd.read_csv(csv_path)
    # Second, making some titles
    st.subheader("🎵 Spotify Data Preview")
    st.write("Below find the cleaned up data set with thousands of songs! 🎷 ")

    # Third, Let's clean up the data set a little bit
    df_clean = df.drop(columns=['track_id', 'duration_ms', "Unnamed: 0"]) # This line allows me to drop some files that I didn't want showing
    df_clean.columns = df_clean.columns.str.replace('_', ' ', regex=False).str.title() # This makes the titles a little more clean with no "_"
    st.dataframe(df_clean)

    # Fourth, lets add some stuff

    # 🔍 Add Filter Options
    st.subheader("🔎 Filter the Music Data")

    

    # Create sidebar or expandable filters if needed
    filter_by = st.selectbox("Choose what you'd like to filter by:", 
                             ["None", "Track Genre", "Artist", "Popularity", "Tempo", "Energy", "Instrumentalness", "Valence", "Liveness", "Acousticness", "Speechiness", "Loudness", "Danceability"])

    # Apply selected filter
    if filter_by == "Track Genre":
        genres = df_clean['Track Genre'].dropna().unique()
        selected_genre = st.selectbox("Select a genre:", sorted(genres))
        filtered_df = df_clean[df_clean['Track Genre'] == selected_genre]
        st.write(f"Showing songs in the **{selected_genre}** genre:")
        st.dataframe(filtered_df)
    elif filter_by == "Artist":
        artists = df_clean['Artists'].dropna().unique()
        selected_artist = st.selectbox("Select an artist:", sorted(artists))
        filtered_df = df_clean[df_clean['Artists'] == selected_artist]
        st.write(f"Showing songs by **{selected_artist}**:")
        st.dataframe(filtered_df)
    elif filter_by == "Popularity":
        min_pop = int(df_clean['Popularity'].min())
        max_pop = int(df_clean['Popularity'].max())
        selected_range = st.slider("Select popularity range:", min_pop, max_pop, (50, 100))
        filtered_df = df_clean[
            (df_clean['Popularity'] >= selected_range[0]) & (df_clean['Popularity'] <= selected_range[1])
        ]
        st.write(f"Showing songs with popularity between {selected_range[0]} and {selected_range[1]}:")
        st.dataframe(filtered_df)
    elif filter_by == "Tempo":
        min_tempo = float(df_clean['Tempo'].min())
        max_tempo = float(df_clean['Tempo'].max())
        selected_tempo = st.slider("Select tempo range:", float(min_tempo), float(max_tempo), (90.0, 130.0))
        filtered_df = df_clean[
            (df_clean['Tempo'] >= selected_tempo[0]) & (df_clean['Tempo'] <= selected_tempo[1])
        ]
        st.write(f"Showing songs with tempo between {selected_tempo[0]:.1f} and {selected_tempo[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    elif filter_by == "Energy":
        min_energy = float(df_clean['Energy'].min())
        max_energy = float(df_clean['Energy'].max())
        selected_energy = st.slider("Select Energy Level:", float(min_energy), float(max_energy), (0.0, 0.9999))
        filtered_df = df_clean[
            (df_clean['Energy'] >= selected_energy[0]) & (df_clean['Tempo'] <= selected_energy[1])
        ]
        st.write(f"Showing songs with tempo between {selected_energy[0]:.1f} and {selected_energy[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    elif filter_by == "Instrumentalness":
        min_Instrumentalness = float(df_clean['Instrumentalness'].min())
        max_Instrumentalness = float(df_clean['Instrumentalness'].max())
        selected_Instrumentalness = st.slider("Select Instrumentalness Level:", float(min_Instrumentalness), float(max_Instrumentalness), (0.0, 0.9999))
        filtered_df = df_clean[
            (df_clean['Instrumentalness'] >= selected_Instrumentalness[0]) & (df_clean['Instrumentalness'] <= selected_Instrumentalness[1])
        ]
        st.write(f"Showing songs with Instrumentalness between {selected_Instrumentalness[0]:.1f} and {selected_Instrumentalness[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    else:
        st.info("Use the dropdown above to filter the dataset.")

# Tab 2 - Mood Quiz (5 Questions and Result)
with tab2:
    st.header("📝 Mood Quiz")
    st.write("Let's take a look at what kind of mood you're feeling right now")
    
    mood_scores = { 
        "Happy" : 0, 
        "Sad" : 0, 
        "Chill" : 0, 
        "Excited" : 0,
        "Quiet" : 0
    }

    # -- Question 1 -- 
    st.markdown("#### **1.Okay whats the plan for the next couple of hours?**")
    Question_one = st.radio(
        "",
        ("Going to a party 💃" , "Staying home and reading 📖", " Hang out with Friends 👯", "Sitting in bed eating ice cream 🍨", "Do Nothing 🤷‍♀️")
                            )
    if Question_one == "Going to a party 💃":
        mood_scores["Excited"] += 1 
    elif Question_one == "Staying home and reading 📖":
        mood_scores["Chill"] +=  1
    elif Question_one == "Hang out with Friends 👯":
        mood_scores["Happy"] += 1
    elif Question_one == "Sitting in bed eating ice cream 🍨":
        mood_scores["Sad"] += 1
    elif Question_one == "Do Nothing 🤷‍♀️" : 
        mood_scores["Quiet"] += 1

    # -- Question 2 -- 
    st.markdown("#### **2.What are we drinking right now?**")
    Question_two = st.radio(
        "",
        ("🍸" , "Tea & Honey 🫖", "Coffee ☕️", "Water 💧", "Milkshake 🥤")
    )

    if Question_two == "🍸":
        mood_scores["Excited"] += 1 
    elif Question_two == "Tea & Honey 🫖":
        mood_scores["Chill"] +=  1
    elif Question_two == "Coffee ☕️":
        mood_scores["Happy"] += 1
    elif Question_two == "Milkshake 🥤":
        mood_scores["Sad"] += 1
    elif Question_two == "Water 💧 " : 
        mood_scores["Quiet"] += 1

    # -- Question 3 -- 
    st.markdown("#### **3.What was the outfit vibe of the day?**")
    Question_three = st.radio(
        "",
        ("Sweats and Hoodie 🧥" , "PJs! 🧦" ,  "Dressed Up 🕺" , "Jeans and a Top 👚", "Something basic 👔")
    )

    if Question_three == "Dressed Up 🕺":
        mood_scores["Excited"] += 1 
    elif Question_three == "PJs! 🧦":
        mood_scores["Chill"] +=  1
    elif Question_three == "Jeans and a Top 👚":
        mood_scores["Happy"] += 1
    elif Question_three == "Sweats and Hoodie 🧥":
        mood_scores["Sad"] += 1
    elif Question_three == "Something basic 👔" : 
        mood_scores["Quiet"] += 1

     # -- Question 4 -- 
    st.markdown("#### **4.What would you like to do for fun?**")
    Question_four = st.radio(
        "",
        ("Cook 🧑‍🍳" , "Read a Book 📚" ,  "Hang with Friends 😜" , "Go Out 🎉 ", "Be alone 🙂")
    )

    if Question_four == "Go Out 🎉 ":
        mood_scores["Excited"] += 1 
    elif Question_four == "Cook 🧑‍🍳":
        mood_scores["Chill"] +=  1
    elif Question_four == "Hang with Friends 😜":
        mood_scores["Happy"] += 1
    elif Question_four == "Be alone 🙂":
        mood_scores["Sad"] += 1
    elif Question_four == "Read a Book 📚 " : 
        mood_scores["Quiet"] += 1

     # -- Question 5 -- 
    st.markdown("#### **5.Whats your favorite color?**")
    Question_five = st.radio(
        "",
        ("Red 🍓" , "Green 🌲" ,  "Yellow 🍋" , "Blue 🐟", "Brown 🐻")
    )

    if Question_five == "Red 🍓 ":
        mood_scores["Excited"] += 1 
    elif Question_five == "Green 🌲":
        mood_scores["Chill"] +=  1
    elif Question_five == "Yellow 🍋":
        mood_scores["Happy"] += 1
    elif Question_five == "Blue 🐟":
        mood_scores["Sad"] += 1
    elif Question_five == "Brown 🐻" : 
        mood_scores["Quiet"] += 1
    
    # --- Submit Button & Result Button --- 
    if st.button("Submit Quiz!"):
    # Determine the mood with the highest score
        detected_mood = max(mood_scores, key=mood_scores.get)

        st.subheader(f"Listen to music that follows this...{detected_mood}!")

# Tab 3 - Recomendations (Based on mood you should listen to ...)
with tab3:
    st.header("🎵 Music Recommendation ")
    st.write("So, don't forget your what mood you were given based on your quiz OR what you're feeling right now! Below find some" \
    "peramiters that you can use to zone in on what kind of music you want to hear. Simply follow the BLHA BLAH BLAH BLAH")


# Tab 4 - About
with tab4:
    st.header(" ℹ️ About")
    st.write("This app was built to help you discover new music based on your mood. Enjoy!")

