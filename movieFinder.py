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
            # print(response.status_code)
            # print(response.json())
            data = response.json()
            if response.status_code == 200:
                if data.get('Response') == 'True':
                    print('**********************************')
                    print('Movie Title: ', data.get('Title'))
                    print('Movie Year: ', data.get('Year'))
                    print('Movie Rated: ', data.get('Rated'))
                    print('Movie Award: ', data.get('Award'))
                    print('Movie BoxOffice: ', data.get('BoxOffice'))
                    print('Movie Write: ', data.get('Director'))
                    print('Movie Write: ', data.get('Writer'))
                    print('**********************************')
                else:
                    print('**********************************')
                    print(f'No movies exist with this {title}')
                    print('**********************************')
        except Exception as e:
            print(e)


api_key = '42527132'
# create object
movie = MovieDescription(api_key)

# while loop to run program continuosly
while True:
    try:
        title = input('Enter movie title: ')
        print('Searching movie...........')
        # call method
        movie.searched_movie(title)
        choice = input('Would you like to continue? (y/n): ').lower()
        if choice == 'y' or choice == 'yes':
            continue
        elif choice == 'n' or choice == 'no':
            print('**************************************')
            print('Thankyou for using movie finder app..')
            print('**************************************')
            break
        else:
            print('**************************************')
            print('Invalid input, please try again!!')
            print('**************************************')
    except Exception as e:
        print(e)