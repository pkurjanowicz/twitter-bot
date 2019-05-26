import datetime
from authentication import api
import requests

 #message = "The time is {}. Do you know where your twitter bot is?".format(
 #    datetime.datetime.now().strftime('%-I:%m %p'))
 #print('posting this clever message to twitter:')
 #print(message)

 #api.update_status(message)
word = input("What word would you like to rhythm with?")

response = requests.get("https://rhymebrain.com/talk?function=getRhymes&word="+word)

rhymes = response.json()

tweet = ""
counter = 0
for rhyme in rhymes:
    if counter <= 5:
        tweet += rhyme["word"] + " "
        counter += 1
print(tweet)

api.update_status(tweet)

print('success!')
