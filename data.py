users = [ 
    {
        "name": "Abdul", 
        "age": 22, 
        "location": "Chicago, IL", 
        "hobbies": ["Fishing", "Cooking"], 
        "pet": {
            "name": "Cookie", 
            "kind": "cat"
            }
    },
    {
        "name": "John", 
        "age": 98, 
        "location": "San Jose", 
        "hobbies": ["Fishing", "Cooking"], 
        "pet": {
            "name": "Pancake", 
            "kind": "rat"
            }
    },
    {
        "name": "Jose", 
        "age": 22, 
        "location": "Florida", 
        "hobbies": ["Hunting", "Eating"], 
        "pet": {
            "name": "Cookie", 
            "kind": "cat"
            }
    },
    {
        "name": "Abdul", 
        "age": 22, 
        "location": "Chicago, IL", 
        "hobbies": ["Fishing", "Cooking"], 
        "pet": {
            "name": "Pumpkin", 
            "kind": "dog"
            }
    },
    {
        "name": "James", 
        "age": 22, 
        "location": "New York, NY", 
        "hobbies": ["Exotic Cars", "Racing"], 
        "pet": {
            "name": "Mustang", 
            "kind": "Tiger"
            }
    }
]

# maping - meaning search

locations = [] # - list of strings
pets = [] # - list of dictionary
hobbies = [] # - list of list

# step 1 : print(users) and now we need to loop through this 
#loop and print only names:
for user in users:
    print(user["name"])

for user in users:
   # print(user["location"])
    locations.append(user["location"])

    # print(user["pet"]["kind"]) - user has a list of objects and we can list them all by adding more lists
    pets.append(user["pet"] ["kind"])

    # print(user["hobbies"])
    hobbies.append(user["hobbies"])
    
print(locations)
print(pets)
print(hobbies)
   


