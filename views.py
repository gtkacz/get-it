from urllib.parse import unquote_plus
from utils import *
from database import Database, Note

def request_params(request):
    request = request.replace('\r', '')
    partes = request.split('\n\n')
    corpo = partes[1]
    params = {}
    for valor in corpo.split('&'):
        key = unquote_plus(valor.split('=')[0])
        value = unquote_plus(valor.split('=')[1])
        params[key] = value
    return params

def index(request):
    note_template = load_template('components/note.html')
    dados=Database('notes')
    db_notes=dados.get_all()
    
    if request.startswith('GET'):
        # Cria uma lista de < li > 's para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        notes_li = [
            note_template.format(title = dados.title, details = dados.content, id=dados.id)
            for dados in db_notes
        ]
        notes = '\n'.join(notes_li)
        return build_response() + load_template('index.html').format(notes = notes).encode(encoding = 'utf-8')
    
    elif request.startswith('POST'):
        params = request_params(request)
        
        is_restore=False
        is_delete=False
        is_edit=False
        
        if (request.split()[-1]).split('&')[-1]=='restore-db=restore-db':
            is_restore=True
            
        if ((request.split()[-1]).split('&')[-1]).split('=')[0]=='delete_note_id':
            is_delete=True
            note_id=((request.split()[-1]).split('&')[-1]).split('=')[1]
            dados.delete(note_id)
            
        if ((request.split()[-1]).split('&')[-1]).split('=')[0]=='edit_note_id':
            is_edit=True
            note_id=((request.split()[-1]).split('&')[-1]).split('=')[1]
            note_title=unquote_plus((request.split()[-1]).split('&')[0]).split('=')[1]
            note_content=unquote_plus((request.split()[-1]).split('&')[1]).split('=')[1]
            
            edit=Note()
            edit.id=note_id
            edit.title=note_title
            edit.content=note_content
            dados.update(edit)
        
        if (is_restore == False) and (is_delete == False) and (is_edit == False):
            write_on_db(params, 'notes')
            
        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')