import os
import uuid

def save_uploaded_file(uploaded_file, subfolder):
    # Ensure the folder exists
    folder_path = os.path.join("assets", subfolder)
    os.makedirs(folder_path, exist_ok=True)

    # Create a unique filename
    ext = os.path.splitext(uploaded_file.name)[1]
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    full_path = os.path.join(folder_path, unique_filename)

    with open(full_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return full_path
