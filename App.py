import streamlit as st
import pandas as pd
import random
import time
import gdown

# Funktion zum Laden der Datei automatisch von Google Drive
def load_data_from_drive():
    # Google Drive-Link
    url = "https://drive.google.com/uc?id=1IIQhp6BT9nmWvZYByedjLKV1ifX8PrIm"  # Ersetze dies mit dem korrekten ID-Link
    output_path = "/mnt/data/tatoeba_data.tsv"  # Speicherort für die heruntergeladene Datei

    # Datei von Google Drive herunterladen
    gdown.download(url, output_path, quiet=False)

    try:
        # TSV-Datei einlesen
        data = pd.read_csv(output_path, sep="\t", header=None, usecols=[1, 3], on_bad_lines="skip")

        # Überprüfen, ob mindestens 2 Spalten vorhanden sind
        if data.shape[1] < 2:
            st.error(f"Die hochgeladene Datei enthält {data.shape[1]} Spalten. Erwartet werden mindestens 2 Spalten.")
            return None
        return data
    except pd.errors.ParserError as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return None

# Streamlit app layout
st.title("Tatoeba Satzanzeige mit Fade-Effekt")

# Datei automatisch von Google Drive laden
data = load_data_from_drive()

# Wenn die Daten geladen wurden, Sätze anzeigen
if data is not None:
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

    # Wiederholter Wechsel der Sätze
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
