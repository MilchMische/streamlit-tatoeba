import streamlit as st
import pandas as pd
import random
import time

# Funktion zum Laden der Datei, wenn sie manuell hochgeladen wird
def load_data(uploaded_file):
    try:
        data = pd.read_csv(uploaded_file, sep='\t', header=None)
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
    
    # Datei hochladen
    uploaded_file = st.file_uploader("Wählen Sie eine TSV-Datei aus", type="tsv")
    
    if uploaded_file is not None:
        # Lade die Daten aus der hochgeladenen Datei
        data = load_data(uploaded_file)
        show_sentences(data)  # Zeige die Sätze mit der Animation

if __name__ == "__main__":
    main()
