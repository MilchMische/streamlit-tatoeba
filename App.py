import streamlit as st
import pandas as pd
import random
import time

# URL for the TSV file
url = "https://tatoeba.org/de/exports/download/55588/Satzpaare%20Italienisch-Englisch%20-%202024-12-05.tsv"

# Function to load data from the URL
def load_data(url):
    data = pd.read_csv(url, sep="\t")
    return data

# Load the dataset
data = load_data(url)

# Set the title for the Streamlit app
st.title("Tatoeba Sentence Pair Display")

# Display one sentence and its translation
if st.button("Show Random Sentence Pair"):
    # Pick a random row from the dataset
    random_row = data.sample(1).iloc[0]
    
    # Display the sentence and its translation
    italian_sentence = random_row['Italian']
    english_translation = random_row['English']
    
    st.subheader("Italian Sentence:")
    st.write(italian_sentence)
    
    # Pause for 3 seconds before showing the translation
    time.sleep(3)
    
    st.subheader("English Translation:")
    st.write(english_translation)
