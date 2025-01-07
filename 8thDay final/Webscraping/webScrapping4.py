import requests

# Authentication
url = 'https://httpbin.org/get'
username = 'user'
password = 'pass'

resp = requests.get(url, auth=(username, password))

if resp.status_code == 200:
    print('Authentication successful!')
    print(resp.text)
else:
    print(f'Authentication failed. Status code: {resp.status_code}')