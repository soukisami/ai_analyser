import os
import json
from datetime import datetime

def store_product_idea(idea: str, storage_path="ideas.json"):
    # Ensure folder exists if using subfolder
    folder = os.path.dirname(storage_path)
    if folder:
        os.makedirs(folder, exist_ok=True)

    data = {
        "idea": idea,
        "timestamp": datetime.now().isoformat()
    }

    # Create file if it doesn't exist
    if not os.path.exists(storage_path):
        with open(storage_path, "w") as f:
            json.dump([], f)

    # Load existing ideas
    with open(storage_path, "r") as f:
        ideas = json.load(f)

    # Add the new idea
    ideas.append(data)

    # Save back to file
    with open(storage_path, "w") as f:
        json.dump(ideas, f, indent=4)
