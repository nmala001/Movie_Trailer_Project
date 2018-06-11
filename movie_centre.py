import movie_search
import config
from Media import Movie
from fresh_tomatoes import open_movies_page

movie_search.YOUTUBE_API_KEY = config.YOUTUBE_API_KEY
movie_search.OMDB_API_KEY = config.OMDB_API_KEY

BatMan = Movie.movie('BatMan')
INCEPTION = Movie.movie('Inception')
BLADE_RUNNER = Movie.movie('Blade Runner', '1982')
Avatar = Movie.movie('Avatar')
SNATCH = Movie.movie('Snatch')
BRICK = Movie.movie('Brick')
PRIMER = Movie.movie('Primer')
MAD_MAX = Movie.movie('Mad Max', '2015')
Rangasthalam = Movie.movie('Rangasthalam')
Teen_Titans_Go = Movie.movie('Teen_Titans_Go')

movies = [INCEPTION, PRIMER, SNATCH, MAD_MAX, BLADE_RUNNER,
          BRICK, Rangasthalam, Avatar, BatMan, Teen_Titans_Go]

open_movies_page(movies)  # Generate HTML and open in browser
