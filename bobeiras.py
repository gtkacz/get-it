from utils import has_directory, load_data
from pathlib import Path

#print(has_directory('./templates/teste.html', 'templates'))

print(type(load_data(Path('./notes.json'))))