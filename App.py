import streamlit as st
import pandas as pd
import random
import time

# Function to load data from the uploaded file
def load_data(uploaded_file):
    try:
        # Read the uploaded TSV file and skip lines with unexpected number of fields
        data = pd.read_csv(uploaded_file, sep="\t", on_bad_lines="skip")  # Skip problematic lines
        return data
    except pd.errors.ParserError as e:
        st.error(f"Error loading data: {e}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None

# Set the title for the Streamlit app
st.title("Tatoeba Sentence Pair Display")

# File uploader for the user to upload a TSV file
uploaded_file = st.file_uploader("Upload your TSV file", type=["tsv"])

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Load the dataset
    data = load_data(uploaded_file)

    # If data is loaded, display it
    if data is not None:
        # Display the column names for debugging
        st.write("Column names in the uploaded file:", data.columns)

        # Display one sentence and its translation
        if st.button("Show Random Sentence Pair"):
            # Pick a random row from the dataset
            random_row = data.sample(1).iloc[0]
            
            # Try to access 'Italian' and 'English' columns
            italian_sentence = random_row.get('Italian', None)
            english_translation = random_row.get('English', None)

            if italian_sentence is not None and english_translation is not None:
                st.subheader("Italian Sentence:")
                st.write(italian_sentence)

                # Pause for 3 seconds before showing the translation
                time.sleep(3)

                st.subheader("English Translation:")
                st.write(english_translation)
            else:
                st.error("The expected columns ('Italian' and 'English') were not found in the file.")
    else:
        st.error("Failed to load the dataset.")
else:
    st.info("Please upload a TSV file to get started.")
