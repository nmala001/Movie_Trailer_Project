import webbrowser
import movie_search

Youtube_URL = 'https://www.youtube.com/watch?v={}'

# A class is used for encapsulating the movie info
# Movie instances are created that are used by fresh_tomatoes.py to render the website's HTML

class Movie:
    
    # A constructor for the 'Movie' class has been created and also instance for the Movie attributes are set.

    def __init__(self, title, plot, trailer_youtube_url, poster_image_url, movie_data=None):

        self.title = title
        self.plot = plot
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.movie_data = movie_data
    
    def show_trailer(self):

        # Opens youtube trailer in the web browser

        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):

        # Opens the poster image url in the web browser

        webbrowser.open(self.poster_image_url)
    
    @staticmethod

    def movie(movie_title, year=None):

        movie_data = Movie.get_movie_data(movie_title, year)

        title = movie_title
        plot = movie_data['plot']
        trailer_youtube_url = movie_data['youtube_url']
        poster_image_url = movie_data['poster']

        return Movie(title, plot, trailer_youtube_url, poster_image_url, movie_data)
    
    @staticmethod

    # The data is fetched using Youtube API and OMDB API
    def get_movie_data(movie_title, year=None, *queries):

        movie_info = movie_search.omdb_movie_info(movie_title, year)
        video_id = movie_search.youtube_video_id(movie_title, year, *queries)
        
        # Adding the Youtube data to the dictionary
        data = movie_info

        data['youtube_id'] = video_id
        data['youtube_url'] = Youtube_URL.format(video_id)

        return data










