import json

def readJson(path_):  
    '''
    Return a dict or a list of dicts from a given JSON.
    '''
    with open(path_) as j:
        return json.load(j)

def writeJson(filename:str,source:list[dict],):
    '''
    Writes a list of dicts to a JSON file.
    Filename = example.json
    Source = list of dictionaries.
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(source, f, ensure_ascii=False, indent=4)