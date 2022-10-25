import json, requests, os

zsh_env_token = "dop_my_secret_token"
#os.getenv('token')

def get_droplets(do_token):
    url = 'https://api.digitalocean.com/v2/droplets'
    two_headers = {"Content-Type": "application/json","Authorization": "Bearer" + do_token}

    response = requests.get(url, headers=two_headers)
    resp = response.json()
    return resp

print(get_droplets(do_token=zsh_env_token))