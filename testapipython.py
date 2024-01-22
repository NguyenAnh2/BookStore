import requests

url = 'http://localhost:3000/sach'

response = requests.get(url).json()

# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Request failed with status code: {response.status_code}")
