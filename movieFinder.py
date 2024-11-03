# movie finder app
import requests

class MovieDescription:
    # constructor
    def __init__(self, api_key):
        self.api_key = api_key
    
    # method
    def searched_movie(self, title):
        try:
            url = f'http://www.omdbapi.com/?t={title}&apikey={self.api_key}'
            response = requests.get(url)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print(e)


api_key = '42527132'
# create object
movie = MovieDescription(api_key)
title = input('Enter movie title: ')
# call method
movie.searched_movie(title)
