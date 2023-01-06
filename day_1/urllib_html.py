import urllib.request

# OPen http://www.py4inf.com/code/romeo.txt using urllib 
with urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt') as url:
    fhand = url.read().decode().split("\n")

    count = 0
    # Loop through each line of the file
    for line in fhand:
        print(line.strip())
        count += len(line.split()) # Split the line using " " (space) and add the length to the count

    print("Word count: ", count)
