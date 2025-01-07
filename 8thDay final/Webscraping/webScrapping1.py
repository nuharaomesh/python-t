import requests

resp = requests.get("https://api.github.com/events")

if resp.status_code == 200:
    
    print("Success")
    
    # Reading response header
    print(resp.headers)
    
    # Check response content type
    content_type = resp.headers['Content-type']
    print(content_type)
    
    # Reading content of response
    print(type(resp.text))