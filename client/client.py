import requests

endpoint_GET = "http://localhost:8000/api/products/1/"
endpoint_POST = "http://localhost:8000/api/"

get_response = requests.get(endpoint_GET)
post_response = requests.post(endpoint_POST, json={'title': 'Hello World5', 'content': 'Hello World content', 'price': 12})

print(get_response.json())
print(post_response.json())