from database import Database, Note
from utils import load_data
import os

def POPULATE_DB(DB_NAME):
    DB_PATH=DB_NAME + '.db'
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    db = Database(DB_NAME)
    json_path = load_data('./data/notes.json')

    for i in json_path:
        annotation = Note()
        annotation.title = list(i.values())[0]
        annotation.content = list(i.values())[1]
        db.add(annotation)
        
POPULATE_DB('notes')