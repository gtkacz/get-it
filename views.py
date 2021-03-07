from utils import load_data, load_template
from urllib.parse import unquote_plus
from utils import has_directory, build_response
import json

def request_params(request):
    request = request.replace('\r', '')
    partes = request.split('\n\n')
    corpo = partes[1]
    params = {}
    for valor in corpo.split('&'):
        key=unquote_plus(valor.split('=')[0])
        value=unquote_plus(valor.split('=')[1])
        params[key]=value
    return params
    
def write_json(data, filename):
    path=has_directory(filename, 'data')
    with open(path,'r', encoding ='utf-8') as file:
        write=json.load(file)
    
    with open(path, 'w') as file:
        write.append(data)
        json.dump(write, file, ensure_ascii=False, indent=4) 

def index(request):
    note_template = load_template('components/note.html')
    if request.startswith('GET'):
        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        notes_li = [
            note_template.format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('notes.json')
        ]
        notes = '\n'.join(notes_li)
        return build_response() + load_template('index.html').format(notes=notes).encode(encoding='utf-8')
    
    elif request.startswith('POST'):
        params = request_params(request)
        
        write_json(params, 'notes.json')
        return build_response(code=303, reason='See Other', headers='Location: /')
            