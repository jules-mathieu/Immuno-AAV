import matplotlib.pyplot as plt
import streamlit as st

# Tracer le graphique
def plot_antibodies_response(days, antibodies, second_injection_day):
    fig, ax = plt.subplots()
    ax.plot(days, antibodies, label="Anticorps")
    ax.axvline(x=second_injection_day, color='red', linestyle='--', label='2e injection')
    ax.set_xlabel("Jours")
    ax.set_ylabel("Concentration relative d'anticorps")
    ax.set_title("Cinétique des anticorps contre AAV")
    ax.legend()
    st.pyplot(fig)
