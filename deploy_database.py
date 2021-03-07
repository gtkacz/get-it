from database import Database, Note
from utils import load_data


db = Database('notes')

for data in load_data('notes.json'):
    title = data['titulo']
    id = None
    details = data['detalhes']
    db.add(Note(id, title, details))
