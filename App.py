import streamlit as st
import pandas as pd
import time

# Funktion zum Laden der hochgeladenen Datei und zur Inspektion des Dateiinhalts
def load_data(uploaded_file):
    try:
        # Datei einlesen und nur die Spalten mit den relevanten Daten behalten
        data = pd.read_csv(uploaded_file, sep="\t", header=None, usecols=[1, 3], on_bad_lines="skip")
        
        # Dateiinformationen anzeigen
        st.write("Vorschau der ersten 5 Zeilen der hochgeladenen Datei:")
        st.write(data.head())  # Zeige die ersten 5 Zeilen der Datei
        
        # Überprüfen, ob mindestens 2 Spalten vorhanden sind
        if data.shape[1] < 2:
            st.error(f"Die hochgeladene Datei enthält {data.shape[1]} Spalten. Erwartet werden mindestens 2 Spalten.")
            return None
        return data
    except pd.errors.ParserError as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return None
    except Exception as e:
        st.error(f"Unerwarteter Fehler: {e}")
        return None

# Titel der Streamlit-App
st.title("✨ Tatoeba Satzpaare-Anzeige ✨")

# Prüfen, ob die Datei schon im Session State gespeichert wurde
if 'data' not in st.session_state:
    # Datei-Upload für den Benutzer
    uploaded_file = st.file_uploader("Lade deine TSV-Datei hoch", type=["tsv"])

    # Wenn eine Datei hochgeladen wird, speichern wir sie im Session State
    if uploaded_file is not None:
        st.session_state['data'] = load_data(uploaded_file)

# Wenn die Datei geladen ist, fahren wir fort
if 'data' in st.session_state and st.session_state['data'] is not None:
    data = st.session_state['data']

    # Platzhalter für die dynamische Satzanzeige
    italian_placeholder = st.empty()
    english_placeholder = st.empty()

    # Button zum Starten der Satzanzeige
    if st.button("Satzpaare anzeigen"):
        for _ in range(10):  # Anzahl der angezeigten Sätze
            # Zufälliges Satzpaar aus den Daten auswählen
            random_row = data.sample(1).iloc[0]
            italian_sentence = random_row[0]  # 1. Spalte: Italienischer Satz
            english_translation = random_row[1]  # 2. Spalte: Englische Übersetzung

            # Satzpaare nur anzeigen, wenn beide Werte vorhanden sind
            if pd.isna(italian_sentence) or pd.isna(english_translation):
                continue

            # Italienischen Satz mit Fade-In und Fade-Out anzeigen
            italian_html = f"""
            <div style="text-align:center; font-size:24px; font-style:italic; color:#333; opacity:1; transition: opacity 3s;">
                🇮🇹 {italian_sentence}
            </div>
            """
            italian_placeholder.markdown(italian_html, unsafe_allow_html=True)

            # 3 Sekunden warten, bevor die englische Übersetzung angezeigt wird
            time.sleep(3)

            # Englische Übersetzung mit Fade-In und Fade-Out anzeigen
            english_html = f"""
            <div style="text-align:center; font-size:24px; color:#007ACC; opacity:1; transition: opacity 3s;">
                🇬🇧 {english_translation}
            </div>
            """
            english_placeholder.markdown(english_html, unsafe_allow_html=True)

            # 3 Sekunden warten, bevor das nächste Paar angezeigt wird
            time.sleep(3)

            # Löschen der alten Sätze
            italian_placeholder.empty()
            english_placeholder.empty()

else:
    st.info("Bitte lade eine TSV-Datei hoch, um zu starten.")
