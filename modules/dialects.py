import streamlit as st

def render():
    st.header("🗣️ Contribute Your Local Dialect or Language")

    name = st.text_input("Your Name")
    language = st.text_input("Language/Dialect Name")
    region = st.text_input("Region/State")
    text_sample = st.text_area("Say something in your dialect")

    audio_file = st.file_uploader("Upload Audio (optional)", type=["mp3", "wav", "m4a"])

    if st.button("Submit"):
        st.success("Thanks for contributing!")
        # 🔧 Later: save to database or CSV
