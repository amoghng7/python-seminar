import xml.etree.ElementTree as ET

data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

# Convert the string representation into a tree of XML nodes
tree = ET.fromstring(data)

# Use find to search for nodes with specific tags and print them
print('Name:',tree.find('name').text)
# USe get to fetch the attributes of a tag
print('Attr:',tree.find('email').get('hide'))