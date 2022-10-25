# classes - group of functions , it is a list for functions

# import json , requests -  we importing the classes that installed. import - build in function , it is checking if module is available or not

# class funtions(): list of functions
#     def name():
#         print("Hello there")
#     def desk():
#         print("Hello there")
#     def table():
#         print("Hello there")


import json, requests

token = 'dop_my_secret_token' # your digital ocean token
url = 'https://api.digitalocean.com/v2/droplets'
two_headers = {"Content-Type": "application/json","Authorization": "Bearer" + token}

response = requests.get(url, headers=two_headers)
print(response)    # output can not be used by other functions