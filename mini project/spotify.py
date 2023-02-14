import json
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyOAuth

username = 'hsj7sxkq9hszo93uqei13o884'
clientID = '04857dcfb612420baf59d1ec15b1b402'
clientSecret = '24af9fea164b43e8b8bc64b377d6e73c'
redirect_Uri = 'http://google.com/callback/'

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=clientID,client_secret=clientSecret,redirect_uri=redirect_Uri, scope='user-read-playback-state,user-modify-playback-state'))

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_Uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  
# To print the response in readable format.
print(json.dumps(user_name, sort_keys=True, indent=4))

while True:
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        # sp.start_playback(uris=['spotify:track:0HUTL8i4y4MiGCPId7M7wb'])
        print(song)
        print('Song has opened in your browser.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")