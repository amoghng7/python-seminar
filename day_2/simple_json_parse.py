import json

input = '''
    [
        { 
            "id" : "001",
            "x" : "2",
            "name" : ["chuck", "Doe"]
        } ,
        { 
            "id" : "009",
            "x" : "7",
            "name" : {"first_name" : "Brent", "last_name" : "something"}
        }
    ]'''

# Loads JSON from the string
info = json.loads(input)

# Print the length of list
print('User count:', len(info), "\n")

# Loop through each object in list and print it's details
for item in info:
    print('Name', item['name']["first_name"], item['name']["last_name"])
    print('Id', item['id'])
    print('Attribute', item['x'])
    print()