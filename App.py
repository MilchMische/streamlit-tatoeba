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
st.title("✨ Tatoeba Sentence Pair Display ✨")

# File uploader for the user to upload a TSV file
uploaded_file = st.file_uploader("Upload your TSV file", type=["tsv"])

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Load the dataset
    data = load_data(uploaded_file)

    # If data is loaded, proceed
    if data is not None:
        # Remove sentence IDs, assuming they're in the first column (adjust if needed)
        data = data.iloc[:, 1:]  # Keep only the actual sentences

        # Create placeholders to dynamically update content
        italian_placeholder = st.empty()
        english_placeholder = st.empty()

        # Button to start displaying sentences
        if st.button("Start Displaying Sentence Pairs"):
            for _ in range(10):  # Adjust number of sentences to display as needed
                # Pick a random sentence pair from the dataset
                random_row = data.sample(1).iloc[0]
                italian_sentence = random_row[0]  # First column is Italian
                english_translation = random_row[1]  # Second column is English

                # Update the placeholders with the sentences
                italian_placeholder.subheader("🇮🇹 Italian:")
                italian_placeholder.markdown(f"<p style='font-size:24px; color:#333; font-style:italic;'>{italian_sentence}</p>", unsafe_allow_html=True)

                # Wait for 3 seconds before showing the translation
                time.sleep(3)

                english_placeholder.subheader("🇬🇧 English Translation:")
                english_placeholder.markdown(f"<p style='font-size:24px; color:#007ACC;'>{english_translation}</p>", unsafe_allow_html=True)

                # Wait another 3 seconds before moving to the next pair
                time.sleep(3)

                # Clear the previous sentences before displaying the next one
                italian_placeholder.empty()
                english_placeholder.empty()
else:
    st.info("Please upload a TSV file to get started.")
