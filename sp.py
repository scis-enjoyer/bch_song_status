import spotipy.util as util
import spotipy
import Creditentials
import json
import time

#### Authorization Code Flow
user = "" #enter ur user name
scope = "user-read-currently-playing"

Creditentials.SetCreditentials()
token = util.prompt_for_user_token(user, scope)
track = spotipy.Spotify(token).current_user_playing_track()

#### 

def current_track_name(token):
    try:
        json_resp = json.loads(json.dumps(spotipy.Spotify(token).current_user_playing_track()))
        track_name = json_resp['item']['name']
        
        return track_name

    except:
        return('error')

def current_track_artist(token):
    try:
        json_resp = json.loads(json.dumps(spotipy.Spotify(token).current_user_playing_track()))
        artists = [artist for artist in json_resp['item']['artists']]
        track_artist = ', '.join([artist['name'] for artist in artists])

        return track_artist

    except:
        return('error')




