import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import ast

nlp = spacy.load("en_core_web_sm")

# Title & Description
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

# Using file_uploaded to allow for users in upload a file OR enter their text into a text box text_area
st.subheader("Lets Get Started! 🎬📚")
text_input = st.text_area("Enter text below:")
uploaded_file = st.file_uploader("Or upload .txt file", type=["txt"])

# Simple Write down of code and example, allowing for the user to follow
st.markdown("👩‍🏫 **Example: Adding Multiple Patterns & labels**")
st.code("""
[
  {"label": "PERSON", "pattern": "Ava"},
  {"label": "ORG", "pattern": "Google"},
  {"label": "GPE", "pattern": "California"}
]
""", language='python')
st.markdown("⬇️ Paste your custom entity patterns in this format.")

#Input Text or File, allowing for them to input the label and the pattern 
st.subheader("Now let's apply some labels and patterns for your text! 🔍")
label_input = st.text_input("What label would you like to apply? ('ORG' or 'GPE')")
pattern_input = st.text_input("What pattern would you like to apply? ('Google' or 'VA')")


# If case they uploada file, first let them know it was uploaded 
# Then try follow the pattern that was inputted UNLESS it does not follow what was listed
if uploaded_file:
    text_input = uploaded_file.read().decode
    st.success = (" Your text file was successfully uploaded! Lets take a look...")

    try:
        custom_patterns = ast.literal_eval(pattern_input)
    except:
        st.error("Pattern input is not valid.")
        custom_patterns = []
        common_labels = [ 
            "PERSON", "ORG", "GPE", "PRODUCT", "EVENT", "DATE", "TIME"
        ]

# Button the Run
# Setting up the entity ruler & getting rid of any prexisting entity ruler
# Then applying the new customer pattern
st.button("Run NER")
if "entity_ruler" in nlp.pipe_names:
    nlp.remove_pipe("entity_ruler")

ruler = nlp.add_pipe("entity_ruler")
custom_pattern = [{"label": label_input.strip().upper(), "pattern": pattern_input.strip()}]
ruler.add_patterns(custom_pattern)
doc = nlp(text_input)

# Displaying the deteced entities in the text WITH their labels through ent in doc.ents & st.markdown
st.subheader("Detected Entities 🕵️‍♂️")
for ent in doc.ents:
    st.markdown(f"`{ent.text}` → **{ent.label_}**")

# This is what provides the visual represetnations/entities that are detected 
st.subheader("Entity Visualization 👓")
html = spacy.displacy.render(doc, style="ent", page=True)
# The entities are color-coded and makes it easier to see
st.components.v1.html(html, height=300, scrolling=True)
