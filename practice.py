import requests

api_key = '726b3b38-85ae-42a9-adf5-738445db0021'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
# word = 'voluminous'
# root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
# final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(url)
result = r.json()
print(result)

for result in result:
    print(result)
