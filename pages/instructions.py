import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config("Instructions","✨",initial_sidebar_state="collapsed")


with st.form("instruction"):
    st.columns(5)[2].header(":red[Instructions]")
    st.text("Before we begin, there are some instructions has to be followed.")


    # st.subheader("Instructions\n_______________________________________________")
    st.text("""Here are some guidelines to follow for a successful and productive online class:

1. Attend class on time and be respectful by staying engaged and focused.
2. Enable your camera to create a more interactive learning experience.
3. Avoid interruptions and distractions during class time.
4. Complete your assignments on schedule to stay on track with the curriculum.
5. Keep the meeting link private and do not share it with anyone outside the class.
6. Participate actively in the class to maximize your learning potential.
7. Treat your classmates and instructor with respect and kindness.
8. As part of our commitment to the environment and community, you are encouraged to plant two trees and donate blood.
9. Attendance is mandatory for all Life Skills Training sessions.
10. Please inform the instructor beforehand if you need to request sick leave.
        
            
    """)


    st.markdown("<br><br><br><br>",unsafe_allow_html=True)
    st.write("I hereby declare that I have read all instructions and I accept them.")

    submit = st.columns(5)[2].form_submit_button("I accept..")
    if submit:
        switch_page('individual_details')
        













with open("style.css") as f:
    style = f.read()
st.markdown(f"<style>{style}</style>",unsafe_allow_html=True)
