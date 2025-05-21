import pandas as pd
import streamlit as st

import streamlit as st
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open("./config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

authenticator.login()


def page_accueil():
    st.title("Bienvenue sur la page d'accueil")
    st.write("Ceci est la page d'accueil de votre application.")


def page_photos_chat():
    st.title("Photos de mon chat")
    st.write("Voici quelques photos de mon chat.")
    # Ajoutez ici le code pour afficher les photos


def main():
    if st.session_state["authentication_status"]:
        # Utilisation de st.columns pour centrer le titre
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")

        # Utilisation de st.sidebar pour la barre latérale
        with st.sidebar:
            # Bouton de déconnexion
            authenticator.logout("Déconnexion")

            # Menu d'arborescence avec streamlit-option-menu
            selected = option_menu(
                menu_title="Menu",  # Titre du menu
                options=["Accueil", "Photos de mon chat"],  # Options du menu
                icons=["house", "camera"],  # Icônes pour chaque option
                menu_icon="cast",  # Icône du menu
                default_index=0,  # Option sélectionnée par défaut
            )

        # Affichage de la page sélectionnée
        if selected == "Accueil":
            page_accueil()
        elif selected == "Photos de mon chat":
            page_photos_chat()

    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Les champs username et mot de passe doivent être remplis")
