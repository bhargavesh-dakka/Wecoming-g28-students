import streamlit as st
import deta
from time import sleep
from streamlit_extras.switch_page_button import switch_page
st.set_page_config("Instructions","✨",initial_sidebar_state="collapsed")


def insert_to_db():
    db = deta.Deta("d0qzwyt1lmi_UCUcbRxy93KBG7jHv5hcQbCWQKB57paF")
    db = db.Base("G28")
    db.insert({
        "name":name,
        "email":email,
        "Qualification":Qualification,
        "python_level":python_level,
        "college_name":college_name,
        "college_place":college_place,
        "Declaration" : True
    })



with st.form(key = "submit"):
    st.columns(2)[1].subheader(f"Enter your details")
    st.divider()
    
    name = st.text_input("Name : *") 
    email = st.text_input("Email : *")
    Qualification = st.text_input("Qualification : *")
    python_level = str(st.slider("Python Skill Level : 0: Beginner - 5: Expert",0,5))
    college_name = st.text_input("College Name : *")
    college_place = st.text_input("College Place : *") 


    submit = st.columns(5)[2].form_submit_button("Submit")
    
    if submit:
        if len(name)<3:
            st.error("Please enter a valid name")
        elif ("@" not in str(email)) and ("." not in str(email)):
            st.error("Please enter a valid email")
        elif name and email and Qualification and python_level and college_name and college_place:
            insert_to_db()
            st.success("Thank you for submitting.")
            sleep(2)
            switch_page("Syllubus")
        else:
            st.error("Please fill all the details")
        









with open("style.css") as f:
    style = f.read()
st.markdown(f"<style>{style}</style>",unsafe_allow_html=True)
