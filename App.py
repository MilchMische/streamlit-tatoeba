import streamlit as st
import gdown
import pandas as pd
import random
import time

# Funktion zum Laden der Datei von Google Drive
def load_data_from_drive():
    url = 'https://drive.usercontent.google.com/download?id=1IIQhp6BT9nmWvZYByedjLKV1ifX8PrIm&export=download&authuser=0&confirm=t&uuid=ef83cedc-bc3a-48d6-ab3c-c2c29955c9779&at=APvzH3qoWFGUm2vYXcR2bDKPOhcw:1733471675277'
    output_path = '/mnt/data/tatoeba_data.tsv'
    gdown.download(url, output_path, quiet=False)
    data = pd.read_csv(output_path, sep="\t", header=None, usecols=[1, 3], on_bad_lines="skip")
    return data

# Streamlit App Layout
st.title("Tatoeba Satzanzeige mit Fade-Effekt")

# Laden der Daten
data = load_data_from_drive()

if data is not None:
    st.write("Daten erfolgreich geladen")

    # Zufällige Auswahl und Anzeige der Sätze
    st.markdown("""
    <style>
    .fade {
        animation: fadeInOut 6s;
    }
    @keyframes fadeInOut {
        0% { opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { opacity: 0; }
    }
    </style>
    """, unsafe_allow_html=True)

    while True:
        # Zufälligen Index für den Satz auswählen
        random_index = random.randint(0, len(data) - 1)

        italian_sentence = data.iloc[random_index, 0]
        english_translation = data.iloc[random_index, 1]

        italian_block = st.empty()
        italian_block.markdown(f"<h3 class='fade'>{italian_sentence}</h3>", unsafe_allow_html=True)
        time.sleep(3)

        english_block = st.empty()
        english_block.markdown(f"<h3 class='fade'>{english_translation}</h3>", unsafe_allow_html=True)
        time.sleep(3)

        italian_block.empty()
        english_block.empty()
