import urllib.parse, urllib.request
import json
import os

# URL to access the API
serviceurl = 'http://api.positionstack.com/v1/forward?'

# Run an infinte loop until empty address is given
while True:
    # Take address as input (1600 Pennsylvania Ave NW, Washington DC)
    address = input("Enter Address: ")

    # If the address is empty ecit
    if len(address) < 1 : break

    # Add API parameters "access_key" and "query"
    url = serviceurl + urllib.parse.urlencode({'access_key': os.environ['GEO_KEY'],
    'query': address})

    print(url)

    # Call the API and read response
    uh = urllib.request.urlopen(url)
    data = uh.read()

    # Print retrieved data length
    print('Retrieved',len(data),'characters')

    try: 
        # Load retrieved data into JSON
        js = json.loads(str(data.decode()))['data']
    except Exception as e: 
        print(e.with_traceback)
        js = None

    # Convert python object into JSON String and print it
    print(json.dumps(js, indent=4))

    # Print the latitude and longitude information from the JSON
    if js:
        lat = js[0]["latitude"]
        lng = js[0]["longitude"]
        print('lat',lat,'lng',lng)
        location = js[0]['label']
        print(location)