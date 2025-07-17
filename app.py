import streamlit as st
from backend.utils import save_uploaded_file
from backend.save_submission import save_submission

# Streamlit page settings
st.set_page_config(page_title="BhashaSanskriti - Cultural Contribution", layout="centered")

st.title("📜 BhashaSanskriti")
st.markdown("**Preserve India's living heritage by contributing local dialects, recipes, folk tales, and more.**")

st.header("📝 Submit Your Contribution")

# Input fields
name = st.text_input("Your Name")
language = st.text_input("Language / Dialect")
category = st.selectbox("Category", ["Greeting", "Folk Tale", "Festival", "Game", "Food", "Other"])
description = st.text_area("Describe your contribution (in brief)", height=150)
location = st.text_input("Location (Village/City, State)")

uploaded_file = st.file_uploader("Upload file (Image/Audio/Video)", type=["png", "jpg", "jpeg", "mp4", "mp3", "wav", "mkv", "avi"])

if st.button("Submit"):
    if not all([name, language, category, description, uploaded_file, location]):
        st.warning("Please fill all fields and upload a file.")
    else:
        # Determine file type and save
        ext = uploaded_file.name.split(".")[-1].lower()
        if ext in ["png", "jpg", "jpeg"]:
            file_type = "image"
        elif ext in ["mp3", "wav"]:
            file_type = "audio"
        elif ext in ["mp4", "mkv", "avi"]:
            file_type = "video"
        else:
            file_type = "other"

        file_path = save_uploaded_file(uploaded_file, file_type + "s")  # folder: images/audios/videos

        # Save metadata
        save_submission(name, language, category, description, file_path, file_type, location)

        st.success("✅ Your contribution has been submitted successfully!")
        st.balloons()
