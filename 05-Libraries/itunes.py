#It turns out apple has their own API for itunes

#Let's visit this url:
#https://itunes.apple.com/search?entity=song&limit=1&term=weezer

#This URL was constructed manually by reading apples documentation 
#for their iTunes API. 

#Breaking the URL down we need to specify that we're looking for 
#songs in their database. If we want to find information about just
#one song we specify that as well. Lastly, if we want to search for
#one song by a specific artist we do that by typing the last part of
#the URL. All of these things are exemplfied in the URL. 

#If we open this link, we end up with a text file in the downloads
#folder. 

#At first glance, the text file might look a bit cryptic. 

#Notice the {} at the beginning and end of the file and 
#the [] in the middle. In between all of this is a bunch of 
#strings and values. These are key-value pairs. 

#What we are looking at is a JSON file (javascript object notation)

#This is technically related to javascript, but JSON itself is 
#typically seen nowadays as a language-agnostic format for 
#exchanging data between computers. 

#What this means is we can use any programming language to read a 
#JSON file. 

#JSON's are a completely text-based format, which means that if 
#we visit the URL what gets downloaded is just a bunch of text 
#formatted in a standard way using things like {}, [], and ""'s 
#that ultimately contain all of the information on Weezer's first 
#song in their database. 

#An API is what we just described in the paragraph above. 
#A mechanism whereby I can access data on someone else's server 
#and integrate it into your own program.

#Let's write a program that does what we just did.
#That is, take the URL and download it's contents onto my device. 

import json
import requests
import sys


#Guarantees the user specifies the name of a file and band name
if len(sys.argv) != 2: 
    sys.exit()

#Now we've got the opportunity to use the requests library
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#What we see on the screen, formatted almost the same as before, but what you'll see is
#that it has been standardized as a python dictionary. What apple is returning is a JSON response
#then python converts it into a dictionary. Python turns the data into key-value pairs. 
#You'll notice that the data is a bit daunting and it's one huge key-value pair.

# print(response.json())

#We can use another library that will allow you format your data a little more 
#cleanly.

#Python comes with another library called json that allows you to manipulate
#JSON data and format it so it is much easier to understand. 

# print(json.dumps(response.json(), indent =2))

#We now see that "resultCount" is a result of us specifying
#we only want to look at 1 song. We also notice that the dict given to us
#contains a second element whose key is "result" and value is a list of dicts
#that holds the information we care about. 

#So, now that we know the contents of the JSON file, how might we access
#the data we actually want ("trackName: " "Buddy Holly") within the list of dicts
#that is itself within a larger dict? 

#Grab the entire json object
o = response.json()

#Loop through the results value (that is a list) and print the current result
#trackName
for result in o["results"]:
    print(result["trackName"])