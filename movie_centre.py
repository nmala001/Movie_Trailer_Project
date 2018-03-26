import movie_search
import config
from Media import Movie
from fresh_tomatoes import open_movies_page

movie_search.YOUTUBE_API_KEY = config.YOUTUBE_API_KEY
movie_search.OMDB_API_KEY = config.OMDB_API_KEY

INCEPTION = Movie.movie('Inception')
BLADE_RUNNER = Movie.movie('Blade Runner', '1982')
PRIMER = Movie.movie('Primer')
MAD_MAX = Movie.movie('Mad Max', '2015')
SNATCH = Movie.movie('Snatch')
BRICK = Movie.movie('Brick')
Rangasthalam = Movie.movie('Rangasthalam')
Avatar = Movie.movie('Avatar')
IronMan = Movie.movie('IronMan')
SpiderMan = Movie.movie('SpiderMan')
BatMan = Movie.movie('BatMan')
Teen_Titans_Go = Movie.movie('Teen_Titans_Go')

movies = [INCEPTION, PRIMER, SNATCH, MAD_MAX, BLADE_RUNNER, BRICK, Rangasthalam, Avatar, IronMan, SpiderMan, BatMan, Teen_Titans_Go]

open_movies_page(movies)  # Generate HTML and open in browser