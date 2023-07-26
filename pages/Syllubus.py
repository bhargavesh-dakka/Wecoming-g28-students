import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config("Syllubus","✨",initial_sidebar_state="collapsed")

with st.form("sy"):
    st.columns(3)[1].header("Syllubus")
    st.divider()
    st.columns(3)[1].image("syllubus.png")
    sy = st.columns(3)[1].form_submit_button("Thank You ...")














with open("style.css") as f:
    style = f.read()
st.markdown(f"<style>{style}</style>",unsafe_allow_html=True)
