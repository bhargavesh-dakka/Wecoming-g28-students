import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
st.set_page_config("Welcome...🙌","✨",initial_sidebar_state="collapsed")
#Welcoming
st.header("Welcome to Python and Machine Learning Course.")
st.divider()

#About
st.subheader(":green[This Course is intended to walk through with Python and Machine Learning]")
st.markdown("<br><br><br><br>",unsafe_allow_html=True)
st.columns(2)[0].text("So what are you waiting for ...")
if st.columns(3)[1].button("Continue our journey 🤩"):
    switch_page("instructions")




with open("style.css") as f:
    style = f.read()
st.markdown(f"<style>{style}</style>",unsafe_allow_html=True)
