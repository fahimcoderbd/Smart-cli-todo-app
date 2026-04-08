"""Application configuration"""

import os

# JSON storage file path
file_path = "core/todos_data/todos_data.json"

# Ensure data directory exists
os.makedirs("core/todos_data", exist_ok=True)
