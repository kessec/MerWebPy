import json
import os
import requests

def query_database(key, word):
    print('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + key)
    r = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + key)
    return r.json()

v = query_database('20b44a3f-4e3c-4e54-80f8-20c725219db8', 'computer')
print(v)