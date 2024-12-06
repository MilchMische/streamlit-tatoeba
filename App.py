import streamlit as st
import pandas as pd

# Funktion zum Laden der hochgeladenen Datei und zur Inspektion des Dateiinhalts
def load_data(uploaded_file):
    try:
        # Datei einlesen und einige Zeilen anzeigen, um den Inhalt zu überprüfen
        data = pd.read_csv(uploaded_file, sep="\t", on_bad_lines="skip", header=None)
        
        # Dateiinformationen anzeigen
        st.write("Vorschau der ersten 5 Zeilen der hochgeladenen Datei:")
        st.write(data.head())  # Zeige die ersten 5 Zeilen der Datei
        
        # Überprüfen, ob mindestens 5 Spalten vorhanden sind
        if data.shape[1] < 5:
            st.error(f"Die hochgeladene Datei enthält {data.shape[1]} Spalten. Erwartet werden mindestens 5 Spalten.")
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
            italian_sentence = random_row[2]  # 3. Spalte: Italienischer Satz
            english_translation = random_row[4]  # 5. Spalte: Englische Übersetzung

            # Satzpaare nur anzeigen, wenn beide Werte vorhanden sind
            if pd.isna(italian_sentence) or pd.isna(english_translation):
                continue

            # Aktualisieren der Platzhalter mit dem italienischen Satz
            italian_placeholder.subheader("🇮🇹 Italienischer Satz:")
            italian_placeholder.markdown(f"<p style='font-size:24px; color:#333; font-style:italic;'>{italian_sentence}</p>", unsafe_allow_html=True)

            # 3 Sekunden warten, bevor die Übersetzung angezeigt wird
            time.sleep(3)

            # Aktualisieren der Platzhalter mit der englischen Übersetzung
            english_placeholder.subheader("🇬🇧 Englische Übersetzung:")
            english_placeholder.markdown(f"<p style='font-size:24px; color:#007ACC;'>{english_translation}</p>", unsafe_allow_html=True)

            # 3 Sekunden warten, bevor das nächste Paar angezeigt wird
            time.sleep(3)

            # Löschen der alten Sätze
            italian_placeholder.empty()
            english_placeholder.empty()
else:
    st.info("Bitte lade eine TSV-Datei hoch, um zu starten.")
