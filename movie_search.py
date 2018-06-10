# The APIs are obtained from the following links
# Youtube API = https://developers.google.com/youtube/v3/getting-started
# OMDB API key: http://www.omdbapi.com

import requests
from googleapiclient.discovery import build

# We will use API keys saved in config.py file

YOUTUBE_API_KEY = 'AIzaSyAsLq6Y7_ccreQK3omR-i1zjTMuQGv2XZI'
OMDB_API_KEY = 'cb657e5c'


def _convert_to_lower(dictionary):

    # A helper method which converts all the keys to lower case
    """
    We use it in the omdb_search to convert the in the API response
    dictionary to lowercase before the function returns
    """
    """
    Args: dictionary (dict): A dictionary
    Returns: The dictionary with the lower case keys
    """
    lower_case_dictionary = dict()

    for key in dictionary:
        value = dictionary[key]
        lower_case_dictionary[str(key.lower())] = str(value)

    return lower_case_dictionary


def youtube_video_id(title, *args):
    """
      The Youtube service object is built and API calls are made

      -We use Google API client library in python and a YOUTUBE API key
       to make API calls to search for the movie trailers.

        -We use the build service object to make API calls
        specific to movie trailers(see the 'payload' variable below)

    Args:
        title(str): The title of the movie to search for
        *args(str or None): More words to add to query
        like the Movie release year

    Returns:
        str: The youtube video ID that corresponds
        to top search result.

    References:
        - https://developers.google.com/youtube/v3/docs/search/list
        - https://developers.google.com/api-client-library/python
    """
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    query = '+'.join(['trailer', title] + [x for x in args if x is not None])

    payload = dict(q=query, part="id", maxResults=1,
                   type='video', topicId='/m/02vxn')

    # Calling the search.list method to call
    # the results matching the query term

    search = youtube.search().list(**payload)
    response = search.execute()

    video_id = response['items'][0]['id']['videoId']

    return str(video_id)


def omdb_movie_info(title, year=None):

    """
      -It places the calls to omdbapi.com using the python request packages.

      - We use this function to create a request payload
        if a valid OMDB API key is given using the request library.

      - It places the GET request to omdbapi.com

      Args:
          title(str): The movie title
          year (str or None): Release year of the movie

      Returns:
          dict: Request response JSON dictionary

    References:
        - http://www.omdbapi.com/
        - http://docs.python-requests.org/en/master/


    """

    omdb_url = 'http://www.omdbapi.com/'

    # Referred omdbapi.com for details on query parameters

    payload = dict(apikey=OMDB_API_KEY, type='movie', t=title, y=year)

    response = requests.get(omdb_url, params=payload)
    response.raise_for_status()

    return _convert_to_lower(response.json())
