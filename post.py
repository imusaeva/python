import requests, os 

token = os.getenv('token')


url = "https://api.digitalocean.com/v2/droplets"
headers = {"Content-Type": "application/json","Authorization": "Bearer" + token}
response = requests.get(url, headers=headers)

print(response)