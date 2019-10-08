import requests

print('Beginning file apps.json download')

url = 'https://raw.githubusercontent.com/AliasIO/Wappalyzer/master/src/apps.json'
r = requests.get(url)

with open('../data/apps.json', 'wb') as f:
    f.write(r.content)

print('File apps.json updated with success!')