# The APIs are obtained from the following links
# Youtube API = https://developers.google.com/youtube/v3/getting-started
# OMDB API key: http://www.omdbapi.com

import requests
from googleapiclient.discovery import build



# We will use API keys saved in config.py file

YOUTUBE_API_KEY = 'AIzaSyAsLq6Y7_ccreQK3omR-i1zjTMuQGv2XZI'
OMDB_API_KEY = 'cb657e5c'

def _convert_to_lower(dictionary):

    #A helper method which converts all the keys to lower case

    lower_case_dictionary = dict()

    for key in dictionary:
        value = dictionary[key]
        lower_case_dictionary[str(key.lower())] = str(value)

    return lower_case_dictionary

def youtube_video_id(title, *args):

    youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)

    query = '+'.join(['trailer', title] + [x for x in args if x is not None])

    payload = dict(q=query, part="id", maxResults=1,type='video', topicId='/m/02vxn')

    #Calling the search.list method to call the results matching the query term

    search = youtube.search().list(**payload)
    response = search.execute()

    video_id = response['items'][0]['id']['videoId']

    return str(video_id)

def omdb_movie_info(title, year=None):

    omdb_url = 'http://www.omdbapi.com/'

    #Referred omdbapi.com for details on query parameters

    payload = dict(apikey=OMDB_API_KEY, type= 'movie', t=title,y=year)

    response = requests.get(omdb_url, params=payload)
    response.raise_for_status()

    return _convert_to_lower(response.json())



