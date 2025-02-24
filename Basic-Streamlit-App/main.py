import pandas as pd
import streamlit as st

# Now, instead of creating a DataFrame manually, we load a CSV file
# This teaches students how to work with external data in Streamlit
df = pd.read_csv("data/penguins.csv")  # Ensure the "data" folder exists with the CSV file
# Display the imported dataset
st.write("Here's the dataset loaded from a CSV file:")
st.dataframe(df)



# Using a selectbox to allow users to filter data by city
# Students learn how to use widgets in Streamlit for interactivity
sex = st.selectbox("Select a Gender", df["sex"].unique())


# Filtering the DataFrame based on user selection
filtered_df = df[df["sex"] == sex]

# Display the filtered results
st.write(f"People in {sex}:")
st.dataframe(filtered_df)

options = st.multiselect(
    "What Species is Your Fav?",
    ["Adelie", "Gentoo", "Chinstrap"],
)

option = st.selectbox(
    "Out of the three, which Penguin do you think is the nicest?",
    ("Adelie", " Gentoo", " Chinstrap"),
)

st.write("You selected:", option)

agree = st.checkbox("Click this box if you love penguins!")

if agree:
    st.write("Great!")

