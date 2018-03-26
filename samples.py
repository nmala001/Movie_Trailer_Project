import config
import movie_search
from Media import Movie

# Applying API keys
movie_search.YOUTUBE_API_KEY = config.YOUTUBE_API_KEY
movie_search.OMDB_API_KEY = config.OMDB_API_KEY

INCEPTION = Movie('Inception',
                  'A thief, who steals corporate secrets through use of'
                  ' dream-sharing technology, is given the inverse task of'
                  ' planting an idea into the mind of a CEO.',
                  'https://www.youtube.com/watch?v=YoHD9XEInc0',
                  'https://goo.gl/NK7fvQ')

print(INCEPTION.title)

print(INCEPTION.plot)

MAD_MAX_DATA = Movie.get_movie_data('Mad Max', '2015')  # passing the year
MAD_MAX = Movie(MAD_MAX_DATA['title'],
                MAD_MAX_DATA['plot'],
                MAD_MAX_DATA['youtube_url'],
                MAD_MAX_DATA['poster'],
                MAD_MAX_DATA)

print(MAD_MAX.title)

print(MAD_MAX.plot)

for key in MAD_MAX.info:
    entry = '{0:>15} -- {1}'.format(key, MAD_MAX.info[key])
    print(entry)

BLADE_RUNNER = Movie.movie('Blade Runner', '1982')  # `year` is optional

print(BLADE_RUNNER.title)
# | Blade Runner
print(BLADE_RUNNER.plot)

for key in BLADE_RUNNER.info:
    entry = '{0:>15} -- {1}'.format(key, BLADE_RUNNER.info[key])
    print(entry)



