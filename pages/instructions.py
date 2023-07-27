import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config("Instructions","✨",initial_sidebar_state="collapsed")


with st.form("instruction"):
    st.columns(5)[2].header(":red[Instructions]")
    st.text("Before we begin, there are some instructions has to be followed.")


    # st.subheader("Instructions\n_______________________________________________")
    st.text("""
    1. Be disciplined and punctual in the class
    2. Turning on the camera
    3. Do not disturb while class is on
    4. Do Assignments on time.
    5. Do not share the meet link with others
    6. Be active in the class
    7. Respect your peers(classmates) and Instructor
    8. You are required to plant 2 trees and donation of blood 
    9. Need to attend all LST(Life Skills Training) sessions
    10. If you want sick leave, you need to mention it 
        before the day in the group.
        
            
    """)


    st.markdown("<br><br><br><br>",unsafe_allow_html=True)
    st.write("I hereby declare that I have read all instructions and I accept them.")

    submit = st.columns(5)[2].form_submit_button("I accept..")
    if submit:
        switch_page('individual_details')
        













with open("style.css") as f:
    style = f.read()
st.markdown(f"<style>{style}</style>",unsafe_allow_html=True)
