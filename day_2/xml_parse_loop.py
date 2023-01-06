import xml.etree.ElementTree as ET

input = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
            <user x="3">
                <id>004</id>
                <name>John</name>
            </user>
        </users>
    </stuff>'''

# Convert the string representation into a tree of XML nodes
stuff = ET.fromstring(input)

# Find all the subtag "user" under the tag "users"
lst = stuff.findall('users/user')
# Print the length of the tags retrieved
print('User count:', len(lst))

# Iterate through all the retrieved tags and print their data
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
    print()