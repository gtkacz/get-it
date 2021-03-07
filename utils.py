from pathlib import Path
import json


def extract_route(request):
    if request.startswith('GET'):
        return request.split()[1][1:]
    elif request.startswith('POST'):
        return ''        

def is_path(subject):
    if not type(subject) is Path:
        return Path(subject)
    else:
        return subject
        
def read_file(path):
    path = is_path(path)
    extension = path.suffix
    target = ['.txt', '.html', '.css', '.js']
    if extension in target:
        with open(path, 'rt', encoding = 'utf-8') as file:
            data = file.read()
        return data.encode(encoding = 'UTF-8')
    else:
        with open(path, 'rb') as file:
            data = file.read()
        return data
    
def has_directory(string, directory):
    c = 0
    string = str(string)
    for i in string:
        if i == '/':
            c += 1
    if c > 1:
        return str(string)
    else:
        return str(f'./{directory}/{string}')

def load_data(path):
    path = has_directory(path, 'data')
    with open(path, encoding = 'utf-8') as file: 
        data = json.load(file)
    return data

def load_template(name):
    path = has_directory(name, 'templates')
    return (read_file(path)).decode(encoding = 'UTF-8')

def build_response(body = '', code = 200, reason = 'OK', headers = ''):
    args = [str(code), reason]
    response = 'HTTP/1.1 ' + (' '.join(args))
    if headers == '':
        response += '\n\n' + body
    else:
        response += '\n' + headers + '\n\n' + body
    return response.encode(encoding = 'UTF-8')