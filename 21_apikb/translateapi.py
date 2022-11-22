import requests

url = 'https://api.mymemory.translated.net/get?'
res = requests.get(url, params={'q':'My name is Samson', 'langpair':'en|es'})

print(res)
print(res.json()['responseData']['translatedText'])