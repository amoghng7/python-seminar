import urllib.request
from bs4 import BeautifulSoup

# Use urllinb to retrieve web page
request = urllib.request.urlopen("http://www.py4inf.com/book.htm")

# Create Beautiful soup object by providing webpage
soup = BeautifulSoup(request.read())

# Retrieven all anchor (<a>) tags in the webpage
# <a style="color: red;" href="https://google.com">Google</a>
tags = soup('a')

# Loop through each tag and print data
for tag in tags:
    print('TAG:',tag) # Prints complete tag
    print('URL:',tag.get('href')) # Prints the data in href attribute
    print('Content:',tag.contents[0]) # Print the content between <a>content</a>
    print('Attrs:',tag.attrs) # Prints all the attributes in the anchor tags
    print()