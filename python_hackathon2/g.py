import requests

response5 = requests.get('https://api-server.dataquest.io/economic_data/countries')
data5 = response5.json()
print(data5)
