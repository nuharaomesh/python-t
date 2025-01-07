import requests

url = 'https://example.com/search'

params = {'q': 'python', 'category': 'books'}

resp = requests.get(url, params)

# check the URL after impl params
print(resp.url) 

# Reading response
print(resp.text) 