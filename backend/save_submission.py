import json
import os
from datetime import datetime

DATA_FILE = "submissions.json"

def save_submission(name, language, category, description, file_path, file_type, location):
    submission = {
        "name": name,
        "language": language,
        "category": category,
        "description": description,
        "file_path": file_path,
        "file_type": file_type,
        "location": location,
        "timestamp": datetime.now().isoformat()
    }

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(submission)
            f.seek(0)
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([submission], f, indent=2, ensure_ascii=False)
