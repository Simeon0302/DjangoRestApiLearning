import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, json={'data': 'Hello World'}, params={'id': 123})

print(response.json())