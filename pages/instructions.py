import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config("Instructions","✨",initial_sidebar_state="collapsed")


with st.form("instruction"):
    st.columns(5)[2].header(":red[Instructions]")
    st.text("Before we begin, there are some instructions has to be followed.")


    # st.subheader("Instructions\n_______________________________________________")
    st.text("""
    1. Be Descipline and Punctual to the Classes
    2. Turning on camera
    3. Do not disturb while class is on
    4. Do Assignments on time.
    5. Do not share Meet link with others
    6. Be active in the class
    7. Resepect Your peers(class mates) and Instructor
    8. Plant 2 trees and Donation of blood 
    9. Need to attend all LST(Life Skills Training) Sessions
    10.If you want a leave, You need to mention it 
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
