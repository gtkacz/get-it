from database import Database, Note
from utils import load_data


db = Database('notes')

for dados in load_data('notes.json'):
    title = dados['titulo']
    id = None
    details = dados['detalhes']
    aa = Note(id, title, details)
    db.add(aa)
