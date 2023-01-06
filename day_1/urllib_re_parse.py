import urllib.request
import re

# Open http://www.py4inf.com/book.htm
html = urllib.request.urlopen("http://www.py4inf.com/book.htm").read()

# Use regular expression to find all links in the webpage
# 
links = re.findall('href="(http://.*?)"', html.decode())

# Loop through each link and print them.
for link in links:
    print(link)