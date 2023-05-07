#create all spotify helper functions for the app
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

#spotify configs
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_url = os.getenv("SPOTIFY_REDIRECT_URL")

scope = ['playlist-modify-public','user-modify-playback-state']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                               redirect_uri=redirect_url, scope=scope))

#spotify functions
def add_song_to_queue(song_url: str):
    try:
        sp.add_to_queue(song_url)
        return " Added track to queue successfully"
    except:
        return "Error adding track to queue"
    
def find_song_by_name(name: str):
    results = sp.search(q=name, type='track')
    if (results):
        song_uri = results['tracks']['items'][0]['uri']
        return song_uri
    
def find_song_by_lyrics(lyrics: str):
    results = sp.search(q=f"lyrics:(lyrics)", type='track')
    if (results):
        if len(results['tracks']['items'])> 0:
            song_uri = results ['tracks']['items'][0]['uri']
            return song_uri
        else:
            return ("No matching tracks found")

def add_song_to_queue_by_song_name(song_name: str):
    song_uri = find_song_by_name(song_name)
    if (song_uri):
        add_song_to_queue(song_uri)
        return " Added track to queue successfully"
    else:
        return "No matching tracks found"
    
def add_song_to_queue_by_lyrics(lyrics: str):
    song_uri = find_song_by_lyrics(lyrics)
    if (song_uri):
        add_song_to_queue(song_uri)
        return " Added track to queue successfully"
    else:
        return "No matching tracks found"  

def start_playing_song_by_name(song_name: str):
    song_uri = find_song_by_name(song_name)
    if song_uri:
        sp.start_playback(uris = [song_uri])
        return f"started playing song (song_name)"
    else:
        return "No matching tracks found"
    
#doesn't work well because of spotify's endpoint
def start_playing_song_by_lyrics(lyrics: str):
    song_uri = find_song_by_lyrics(lyrics)
    if song_uri:
        sp.start_playback(uris = [song_uri])
        return f"started playing song with lyrics: {lyrics}"
    else:
        return "No matching tracks found"  

def start_music():
    try:
        sp.start_playback()
        return "Playback started!"
    except:
        return "Error starting playback"
    
