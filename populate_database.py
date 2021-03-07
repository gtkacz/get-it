from database import Database, Note
from utils import load_data

db = Database('notes')

json_path = load_data('./data/notes.json')

for i in json_path:
    annotation = Note()
    annotation.title = list(i.values())[0]
    annotation.content = list(i.values())[1]
    db.add(annotation)