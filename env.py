import Creditentials
import spotipy
import spotipy.util as util

### Spotify Auth ###

user = "" #enter ur username
scope = "user-read-currently-playing"
Creditentials.SetCreditentials()
token = util.prompt_for_user_token(user, scope)
track = spotipy.Spotify(token).current_user_playing_track()
