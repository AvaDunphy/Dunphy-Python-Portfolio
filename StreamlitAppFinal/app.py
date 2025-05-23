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

#Organize the Tabs on the app, different tabs and labeling the tabs. 
tab1, tab2, tab3, tab4 = st.tabs(["📊 Music Data", "📝 Take Mood Quiz", "🎶 Music Recommendations", "ℹ️ About This App"])

# TAB BY TAB BREAK DOWN 

# Tab 1 - Data Table For Research 
with tab1:
    # Small write up about what the tab is trying to accomplish
    st.header("Let's Look At The Data 👨‍💻")
    st.subheader("What are people listening to? 🤷‍♀️")
    st.write(" With millions of songs out there, it is almost impossible to try and figure out what to listen to. " \
    "So, let me help you out a little! Below find a dataset with thousands of the most popular songs on Spotify. This way if you are unsure what you want to play, " \
    "you can just look below! Also, if you are trying to find a specific artist, genre, song, tempo, or popularity, use the filter " \
    "program to zone in on your search. While looking, please keep in mind that there are so so many songs out in the world, and this data set might not have everything, " \
    "BUT it can sure give you a good idea of what you can listen to." \
    "Thank you! And sit back, relax, and enjoy some good music 🫶🏻")

    # First, inputting the data set into the machine
    csv_path = "StreamlitAppFinal/musicdataset.csv"
    df = pd.read_csv(csv_path)
    # Second, making some titles
    st.subheader("🎵 Spotify Data Preview")
    st.write("Below find the cleaned up data set with thousands of songs! 🎷 ")

    # Third, Let's clean up the data set a little bit using df.drop and .replace
    df_clean = df.drop(columns=['track_id', 'duration_ms', "Unnamed: 0"]) # This line allows me to drop some files that I didn't want showing
    df_clean.columns = df_clean.columns.str.replace('_', ' ', regex=False).str.title() # This makes the titles a little more clean with no "_"
    st.dataframe(df_clean)

    # Fourth, lets add some option for the data
    # Add Filter Options
    st.subheader("🔎 Filter the Music Data")

    # Create sidebar or expandable filters if needed so that they can narrow down what they want to see through selectbox
    filter_by = st.selectbox("Choose what you'd like to filter by:", 
                             ["None", "Track Genre", "Artist", "Popularity", "Tempo", "Energy", "Instrumentalness", "Valence", "Liveness", "Acousticness", "Speechiness", "Loudness", "Danceability"])

    # Apply selected filter & alter based on filter and range of filter (ex Temp has differnt range than Popularity)
    # The code remains some what the same throughout, showing the different filters and the ranges, but they all come from the same data set
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
        selected_tempo = st.slider("Select tempo range:", float(min_tempo), float(max_tempo), (00.0, 247.37))
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
    elif filter_by == "Valence":
        min_Valence = float(df_clean['Valence'].min())
        max_Valence = float(df_clean['Valence'].max())
        selected_Valence = st.slider("Select Valence Level:", float(min_Valence), float(max_Valence), (0.0, 0.9999))
        filtered_df = df_clean[
            (df_clean['Valence'] >= selected_Valence[0]) & (df_clean['Valence'] <= selected_Valence[1])
        ]
        st.write(f"Showing songs with Valence between {selected_Valence[0]:.1f} and {selected_Valence[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    elif filter_by == "Liveness":
        min_Liveness = float(df_clean['Liveness'].min())
        max_Liveness = float(df_clean['Liveness'].max())
        selected_Liveness = st.slider("Select Liveness Level:", float(min_Liveness), float(max_Liveness), (0.0, 0.9999))
        filtered_df = df_clean[
            (df_clean['Liveness'] >= selected_Liveness[0]) & (df_clean['Liveness'] <= selected_Liveness[1])
        ]
        st.write(f"Showing songs with Liveness between {selected_Liveness[0]:.1f} and {selected_Liveness[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    elif filter_by == "Acousticness":
        min_Acousticness = float(df_clean['Acousticness'].min())
        max_Acousticness = float(df_clean['Acousticness'].max())
        selected_Acousticness = st.slider("Select Acousticness Level:", float(min_Acousticness), float(max_Acousticness), (0.0, 0.9999))
        filtered_df = df_clean[
            (df_clean['Acousticness'] >= selected_Acousticness[0]) & (df_clean['Acousticness'] <= selected_Acousticness[1])
        ]
        st.write(f"Showing songs with Acousticness between {selected_Acousticness[0]:.1f} and {selected_Acousticness[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    elif filter_by == "Speechiness":
        min_Speechiness = float(df_clean['Speechiness'].min())
        max_Speechiness = float(df_clean['Speechiness'].max())
        selected_Speechiness = st.slider("Select Speechiness Level:", float(min_Speechiness), float(max_Speechiness), (0.0, 0.9999))
        filtered_df = df_clean[
            (df_clean['Speechiness'] >= selected_Speechiness[0]) & (df_clean['Speechiness'] <= selected_Speechiness[1])
        ]
        st.write(f"Showing songs with Speechiness between {selected_Speechiness[0]:.1f} and {selected_Speechiness[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    elif filter_by == "Loudness":
        min_Loudness = float(df_clean['Loudness'].min())
        max_Loudness = float(df_clean['Loudness'].max())
        selected_Loudness = st.slider("Select Loudness Level:", float(min_Loudness), float(max_Loudness), (-100.0, 100.0))
        filtered_df = df_clean[
            (df_clean['Loudness'] >= selected_Loudness[0]) & (df_clean['Loudness'] <= selected_Loudness[1])
        ]
        st.write(f"Showing songs with Loudness between {selected_Loudness[0]:.1f} and {selected_Loudness[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    elif filter_by == "Danceability":
        min_Danceability = float(df_clean['Danceability'].min())
        max_Danceability = float(df_clean['Danceability'].max())
        selected_Danceability = st.slider("Select Danceability Level:", float(min_Danceability), float(max_Danceability), (0.00, .9999))
        filtered_df = df_clean[
            (df_clean['Danceability'] >= selected_Danceability[0]) & (df_clean['Danceability'] <= selected_Danceability[1])
        ]
        st.write(f"Showing songs with Danceability between {selected_Danceability[0]:.1f} and {selected_Danceability[1]:.1f} BPM:")
        st.dataframe(filtered_df)
    else:
        st.info("Use the dropdown above to filter the dataset.")

# Tab 2 - Mood Quiz (5 Questions and Result)
with tab2:
    st.header("📝 Mood Quiz")
    st.write("Let's take a look at what kind of mood you're feeling right now")
    
    #Establish the inital mood scores for the quiz
    mood_scores = { 
        "Happy" : 0, 
        "Sad" : 0, 
        "Chill" : 0, 
        "Excited" : 0,
        "Quiet" : 0
    }

    # Each question adds up the answers for each equation (similar to Computing I)
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
        ("🥂" , "Tea & Honey 🫖", "Coffee ☕️", "Water 💧", "Milkshake 🥤")
    )

    if Question_two == "🥂":
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

        st.subheader(f"Listen to music that follows a {detected_mood} vibe!")

# Tab 3 - Recomendations (Based on mood you should listen to ...)
with tab3:
    st.header("🎵 Music Recommendation ")
    st.write("Below, input the mood which you received in the previous tab and get some recommendations for songs" \
    "which would go perfectly with the mood! Simply select your mood below.")

    # What is the mood score that the audience recived
    st.subheader(" Select Which Mood You Recived in Tab Two")
    mood_select = st.selectbox("Choose Your Mood:", ["Excited", "Chill", "Happy", "Sad", "Quiet"])

    # Based on what mood are you feeling, you should listen to this song, simple list and markdown
    mood_songs = { 
        "Happy":[
            "1. Dancing Queen - Abba",
                "- https://www.youtube.com/watch?v=xFrGuyw1V8s",
            "2. Lovely Day - Bill Withers",
                "- https://www.youtube.com/watch?v=bEeaS6fuUoA",
            "3. Don't Stop Me Now - Queen",
                "- https://www.youtube.com/watch?v=HgzGwKwLmgM",
            "4. Don't Worry, Be Happy - Bobby McFerrin",
                "- https://www.youtube.com/watch?v=d-diB65scQU",
            "5. Good Vibrations - Beach Boys",
                "- https://www.youtube.com/watch?v=apBWI6xrbLY",
            "6. Unwritten - Natasha Bedingfield",
                "- https://www.youtube.com/watch?v=b7k0a5hYnSI"

        ],
        "Excited":[
            "1. Paper Planes - M.I.A",
                "- https://www.youtube.com/watch?v=ewRjZoRtu0Y",
            "2. Empire State of Mind - Jay Z and Alicia Keys",
                "- https://www.youtube.com/watch?v=tqKWshKUC5E",
            "3. Doses & Mimosas - Cherub",
                "- https://www.youtube.com/watch?v=E45fogGN_Y8",
            "4. I'm So Excited - The Pointer Sisters",
                "- https://www.youtube.com/watch?v=rQqwG_rQx7A",
            "5. I Gotta Feeling - The Black Eyed Peas",
                "- https://www.youtube.com/watch?v=ipii7KbbJLY",
            "6. Shake It Off - Taylor Swift",
                "- https://www.youtube.com/watch?v=mvVBuG4IOW4"

        ],
        "Chill" :[
            "1. Time Moves Slow - BADBADNOTGOOD",
                "- https://www.youtube.com/watch?v=UWIIPX_5rbM",
            "2. Blondie - Current Joys",
                "- https://www.youtube.com/watch?v=-dFHXd1dTSk",
            "3. My Kind of Woman - Mac DeMarco",
                "- https://www.youtube.com/watch?v=_R3B2Xr8kwQ",
            "4. Tommy's Party - Peach Pit",
                "- https://www.youtube.com/watch?v=iMUbmiXlHww"
            "5. Bad Habit - Steve Lacy",
                "- https://www.youtube.com/watch?v=S2PVsv2K1Bg"
            "6. Today - Q",
                "- https://www.youtube.com/watch?v=rzh7Fjm_IpI"
        ],
        "Sad" :[
            "1. Looking Out for You - Joy Again",
                "- https://www.youtube.com/watch?v=ZVQDHFgfssM",
            "2. White Ferrari - Frank Ocean",
                "- https://www.youtube.com/watch?v=Dlz_XHeUUis",
            "3. Heart to Heart - Mac DeMarco",
                "- https://www.youtube.com/watch?v=qBoQzo98EpQ",
            "4. If This World Were Mine - Luther Vandross" ,
                "- https://www.youtube.com/watch?v=RkFIkubuYns",
            "5. ROS - Mac Miller",
                "- https://www.youtube.com/watch?v=-2AfeMnpiRI",
            "6. Blind - Sza",
                "- https://www.youtube.com/watch?v=SZbTfC85nVk"
        ],
        "Quiet" :[
            "1. Comming Home - Leaon Bridges",
                "- https://www.youtube.com/watch?v=_buEFASNfjw",
            "2. A Sunday Kind of Love - Etta James",
                "- https://www.youtube.com/watch?v=kl0DehwApzE",
            "3. Dream A Little Dream - The Mamas & The Papas",
                "- https://www.youtube.com/watch?v=BHABfuMFpl0",
            "4. Hypnotized - Fleetwood Mac",
                "- https://www.youtube.com/watch?v=fDzXbdxeeHI",
            "5. Cheek to Cheek - Fred Astaire",
                "- https://www.youtube.com/watch?v=0QYdcHQXwdM",
            "6. Paris City Jazz - Bellaire",
                "- https://www.youtube.com/watch?v=YhHm0C8Jvmc"
        ]
    }

    # Display songs for selected mood
    # Associating what mood and what songs you should then listen to. 
    st.subheader(f"🎶 Songs for a '{mood_select}' Mood")
    for song in mood_songs[mood_select]:
        st.write(f"{song}")
    
    
# Tab 4 - About
## QUESTION WHY CAN'T THE PHOTOS BE ENTERED IN WHAT
# Small write up
with tab4:
    st.header(" ℹ️ About")
    st.write("This app was built to help user find new music based on their mood. I wanted to try and create an app which " \
    "would allow for user to branch out, listening to something new or find the best vibe. I personally am a huge music fan and need music" \
    "every moment of every day in order to be productive. So now, when I am not sure what I should listen to " \
    "I am going to open this app to help me out. 🤗🎻")
    st.subheader("Below find some of my personal favorites on my spotify playlist 🫶🏻")
    st.write("Below Find my Playlist Links")
    st.write("1. [For A Long Drive](https://open.spotify.com/playlist/4Htky418SJdV8wSEuB8qlC?si=37571108c42f4d45)")
    st.write("2. [A Slow Morning](https://open.spotify.com/playlist/7dQHCpjlaDHu4tnqMqVEvZ?si=0b6b8002c9c8411f)")