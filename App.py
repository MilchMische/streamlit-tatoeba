import pandas as pd
import streamlit as st

def load_data(uploaded_file):
    try:
        # Versuche, die Datei einzulesen und nur gültige Zeilen zu verarbeiten
        # Wir setzen auf `on_bad_lines="skip"`, um problematische Zeilen zu überspringen.
        data = pd.read_csv(uploaded_file, sep="\t", header=None, on_bad_lines="skip")

        # Überprüfe, wie viele Spalten die Datei insgesamt hat
        num_columns = data.shape[1]
        
        # Falls weniger als 2 Spalten vorhanden sind, eine Fehlermeldung ausgeben
        if num_columns < 2:
            st.error(f"Die hochgeladene Datei enthält nur {num_columns} Spalten. Es müssen mindestens 2 Spalten vorhanden sein.")
            return None
        else:
            st.write(f"Die Datei hat {num_columns} Spalten.")
        
        # Nur die relevanten Spalten (1. und 3. Spalte) behalten
        data = data.iloc[:, [1, 3]]
        
        return data
    except pd.errors.ParserError as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return None

# Streamlit app layout
st.title("Tatoeba Satzanzeige mit Fade-Effekt")

# Datei hochladen
uploaded_file = st.file_uploader("Lade eine TSV-Datei hoch", type=["tsv"])

# Wenn die Datei hochgeladen wurde, Daten laden und Sätze anzeigen
if uploaded_file is not None:
    data = load_data(uploaded_file)

    if data is not None:
        # Anzeige der geladenen Daten
        st.write(data.head())
