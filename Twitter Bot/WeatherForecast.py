import requests
from authentication import api
from opencage.geocoder import OpenCageGeocode
import tweepy
import random
from City_list import city_list

#finds a random user's screenname given a location
def get_random_screenname(location):
    get_data = []
    for user in tweepy.Cursor(api.search_users, q=location).items(10):
        dict_ = {'screen_name': user.screen_name,
                    }   
        get_data.append(dict_)
    screen_name = "@"+ get_data[random.randint(1,10)]['screen_name']
    return screen_name

#counts the letters in the tweet to make sure it isn't over 280
def letter_count(string):
    counter = 0
    for letter in string:
        counter += 1
    return counter

#uses data from the city_list file to get a random US city
city = city_list[random.randint(1,len(city_list))]
results = geocoder.geocode(city)

#GeoCoder data used to get the coordinates of the city
key = '343f44aa64984a4a8d2048b21c51ab6a'
geocoder = OpenCageGeocode(key)
coordinates = (results[0]['geometry']['lat'],results[0]['geometry']['lng'])
#transpose the coordinates to variables
latitude = str(coordinates[0])
longitude = str(coordinates[1])

#get the forecast at those coordinates
response = requests.get("https://api.darksky.net/forecast/981925581debd1520bb49a32d739ad3b/" + latitude + "," + longitude)
forecast = response.json()

#access the darksky forecast API to pull out data about the forecast in a specific city
current_temp = ("The temperate in "+city+" is currently "+ str(forecast['currently']['temperature'])+ " degrees")
hourly = ("The hourly forecast is "+ str(forecast['hourly']['summary']))
daily = ("The daily forecast is "+ str(forecast['daily']['summary']))

#create the random screen name and forecast tweet info
random_screen_name = str(get_random_screenname(city))
sentence = current_temp + "\n" + hourly + "\n" + daily
print(random_screen_name + " " + sentence )

#execute the tweet and make sure that it isn't over 280 characters
def main():
    if letter_count(sentence) < 280:  
        api.update_status(status = random_screen_name+ " "+ sentence )
        print('success!')
    else:
        print("please try again the string must be under 280 characters")

if __name__ == '__main__':
    main()



