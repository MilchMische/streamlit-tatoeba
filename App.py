import streamlit as st
import pandas as pd
import gdown
import random
import time

# Funktion zum Herunterladen der Datei von Google Drive
def download_file():
    url = 'https://drive.google.com/uc?id=1IIQhp6BT9nmWvZYByedjLKV1ifX8PrIm&export=download'
    output_path = '/mnt/data/tatoeba_data.tsv'
    gdown.download(url, output_path, quiet=False)
    return output_path

# Lade die TSV-Datei
def load_data():
    file_path = download_file()
    try:
        # Datei als DataFrame laden
        data = pd.read_csv(file_path, sep='\t', header=None)
        data.columns = ['Index', 'ID_Italian', 'Italian', 'ID_English', 'English']
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Funktion zum Anzeigen der Sätze mit Fade-Effekten
def show_sentences(data):
    # Streamlit Widgets zum Starten der Animation
    if data is not None:
        sentence_index = random.randint(0, len(data)-1)  # Zufälligen Satz auswählen
        italian_sentence = data.iloc[sentence_index]['Italian']
        english_translation = data.iloc[sentence_index]['English']
        
        # Animation: fade out und fade in
        with st.empty():
            st.markdown(f"<h2 style='text-align: center; color: blue;'>{italian_sentence}</h2>", unsafe_allow_html=True)
            time.sleep(3)
            st.markdown(f"<h3 style='text-align: center; color: green;'>{english_translation}</h3>", unsafe_allow_html=True)
            time.sleep(3)
            st.experimental_rerun()

# Hauptfunktion für die Streamlit-App
def main():
    st.title("Italienische Sätze mit Übersetzung")
    
    data = load_data()  # Lade die Daten
    if data is not None:
        show_sentences(data)  # Zeige die Sätze mit der Animation

if __name__ == "__main__":
    main()
