import streamlit as st

from core.theme import load_theme
from database.database import initialize

from components.hero import hero
from components.features import features
from components.stats import stats
from components.actions import actions
from components.footer import footer

st.set_page_config(
    page_title="AI Mock Interview",
    page_icon="🤖",
    layout="wide"
)

initialize()

load_theme()

hero()

st.write("")
st.write("")

stats()

st.write("")
st.write("")

actions()

st.write("")
st.write("")

features()

st.write("")
st.write("")

footer()