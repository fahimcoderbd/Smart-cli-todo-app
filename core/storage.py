#handle app storage with json persistence
import json
import os
from core import config

#store todos in dictionary => ram (fast o(n))
todos = [
    #demo todo
   """  {
        "id":1,
        "todo":"Coding",
        "completed":False,
        "status":"pending"
    } """
]

#save in json file
def save_in_json(data):
    with open(config.file_path, 'w') as file:
         json.dump(data, file, indent=4)

#load from json file
def load_from_json():
     if not os.path.exists(config.file_path):
        return [] # Return empty list if file doesn't exist
     try:
          with open(config.file_path, 'r') as  file:
               todos_data = file.read().strip()

               #loading data if data exists
               if todos_data:
                    return json.loads(todos_data)
     except (FileNotFoundError, json.JSONDecodeError):
          return []
    #handling errord
     except FileNotFoundError:
           save_in_json(todos)
     except json.JSONDecodeError:
            save_in_json(todos)

load_from_json()