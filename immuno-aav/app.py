# app.py
import streamlit as st
from models import simulate_antibody_response
from plots import plot_antibodies_response

st.title("Simulation de la réponse immunitaire aux vecteurs AAV")

# Interface utilisateur
aav_types = ["AAV1", "AAV9"]
aav_choice = st.selectbox("Choisir un type de vecteur AAV :", aav_types)

second_injection_day = st.slider("Jour de la deuxième injection :", min_value=1, max_value=60, value=30)

peptidase_treatment = st.checkbox("Traitement peptidase ?")

# Placeholder pour afficher plus tard
st.write("### Cinétique des anticorps")

# Simulation
days, antibodies = simulate_antibody_response(second_injection_day, peptidase_treatment, aav_choice)

# Tracer le graphique
plot_antibodies_response(days, antibodies, second_injection_day)
