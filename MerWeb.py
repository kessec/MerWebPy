import requests

def query_database(key, word):
    _ = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + key)
    _ = _.json()
    try:
        returnDict = {
        "word": word,
        "definition": _[0]['shortdef'][0],
        "type": _[0]['fl'],
        "offensive": str(_[0]['meta']['offensive'])
        }
    except:
        returnDict = {
        "word": word,
        "definition": "N/A",
        "type": "N/A",
        "offensive": "N/A"
        }
    return returnDict