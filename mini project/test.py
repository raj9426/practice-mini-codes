# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='04857dcfb612420baf59d1ec15b1b402', 
#                                                  client_secret='24af9fea164b43e8b8bc64b377d6e73c', 
#                                                  redirect_uri='http://google.com/callback/', 
#                                                  scope=['user-library-read', 'user-read-playback-state', 'user-modify-playback-state']))

# results = sp.search("boyz", limit=1, type="track")
# track_id = results['tracks']['items'][0]['id']

# sp.start_playback(device_id=None, context_uri=None, uris=[track_id])









import spotipy

sp = spotipy.Spotify(auth=YOUR_AUTH_TOKEN)

results = sp.search(q='song name', type='track')

track = results['tracks']['items'][0]

sp.start_playback(uris=[track['uri']])
