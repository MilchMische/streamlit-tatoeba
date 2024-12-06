import streamlit as st
import pandas as pd
import random
import time

# Funktion zum Laden der hochgeladenen Datei
def load_data(uploaded_file):
    try:
        # Datei einlesen und fehlerhafte Zeilen überspringen
        data = pd.read_csv(uploaded_file, sep="\t", on_bad_lines="skip")
        return data
    except pd.errors.ParserError as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return None
    except Exception as e:
        st.error(f"Unerwarteter Fehler: {e}")
        return None

# Titel für die Streamlit-App
st.title("✨ Tatoeba Satzpaare-Anzeige ✨")

# Datei-Upload für den Benutzer
uploaded_file = st.file_uploader("Lade deine TSV-Datei hoch", type=["tsv"])

# Überprüfen, ob eine Datei hochgeladen wurde
if uploaded_file is not None:
    # Daten laden
    data = load_data(uploaded_file)

    # Falls Daten erfolgreich geladen wurden
    if data is not None:
        # Spaltennamen und erste Zeilen der Datei anzeigen
        st.write("Spaltennamen in der hochgeladenen Datei:")
        st.write(data.columns)  # Zeigt die Spaltennamen an

        st.write("Erste Zeilen der Datei:")
        st.write(data.head())  # Zeigt die ersten Zeilen zur Überprüfung an

        # Placeholder für die dynamische Aktualisierung
        italian_placeholder = st.empty()
        english_placeholder = st.empty()

        # Button zum Starten der Satzanzeige
        if st.button("Satzpaare anzeigen"):
            for _ in range(10):  # Anzahl der Sätze anpassen
                # Zufälliges Satzpaar aus den Daten auswählen
                random_row = data.sample(1).iloc[0]
                italian_sentence = random_row[0]  # Erste Spalte (ggf. anpassen)
                english_translation = random_row[1]  # Zweite Spalte (ggf. anpassen)

                # Aktualisieren der Platzhalter mit den Sätzen
                italian_placeholder.subheader("🇮🇹 Italienischer Satz:")
                italian_placeholder.markdown(f"<p style='font-size:24px; color:#333; font-style:italic;'>{italian_sentence}</p>", unsafe_allow_html=True)

                # 3 Sekunden warten, bevor die Übersetzung angezeigt wird
                time.sleep(3)

                english_placeholder.subheader("🇬🇧 Englische Übersetzung:")
                english_placeholder.markdown(f"<p style='font-size:24px; color:#007ACC;'>{english_translation}</p>", unsafe_allow_html=True)

                # 3 Sekunden warten, bevor das nächste Paar angezeigt wird
                time.sleep(3)

                # Löschen der alten Sätze vor dem nächsten Durchlauf
                italian_placeholder.empty()
                english_placeholder.empty()
else:
    st.info("Bitte lade eine TSV-Datei hoch, um zu starten.")
