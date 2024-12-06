import streamlit as st
import pandas as pd
import random
import time

# Function to load data from the uploaded file
def load_data(uploaded_file):
    try:
        # Read the uploaded TSV file and skip lines with unexpected number of fields
        data = pd.read_csv(uploaded_file, sep="\t", on_bad_lines="skip")
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

        # Display one sentence and its translation in a loop
        if st.button("Start Displaying Sentence Pairs"):
            for i in range(10):  # Change this value for the number of sentences you want to display
                # Pick a random row from the dataset
                random_row = data.sample(1).iloc[0]

                # Check and adjust the column names based on the actual file content
                italian_sentence = random_row.get(data.columns[0], None)  # First column (likely Italian)
                english_translation = random_row.get(data.columns[1], None)  # Second column (likely English)

                if italian_sentence is not None and english_translation is not None:
                    st.subheader("Italian Sentence:")
                    st.write(italian_sentence)

                    # Pause for 3 seconds before showing the translation
                    time.sleep(3)

                    st.subheader("English Translation:")
                    st.write(english_translation)

                    # Wait for 3 seconds before showing the next pair
                    time.sleep(3)
                else:
                    st.error("Could not find Italian or English columns in the file.")
    else:
        st.error("Failed to load the dataset.")
else:
    st.info("Please upload a TSV file to get started.")
