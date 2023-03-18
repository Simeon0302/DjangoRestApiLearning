import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint)
post_response = requests.post(endpoint, json={'title': 'Hello World', 'content': 'Hello World content', 'price': 12})

print(get_response.json())
print(post_response.json())