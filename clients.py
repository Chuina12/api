import requests
endpoint ='http://127.0.0.1:8000/api_view'
response = requests.post(endpoint,json={'nom':'fgrgt','prenom':'fgrgfrgr'})
print(response.json())

print(response.status_code)
