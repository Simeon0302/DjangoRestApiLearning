import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'This is a test title',
    'price': 12.3
}

response = requests.post(endpoint, json=data)
print(response.json())