import requests

url = 'https://httpbin.org/post'

data = {
        'username': 'user',
        'password': 'pass'
        }

# Requesting post request with user credential for login
resp = requests.post(url, data)

if resp.status_code == 200:
    print('Login successful')
    print(resp.text)
else:
    print('Login failed:', resp.status_code)