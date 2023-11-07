import requests

api_key = 'cdfa6643-3f4c-4480-96cc-d75408db4d92'
word = 'banana'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)