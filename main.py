import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "e97cf6bc063742d8b6f931524b0bc22b"
SPOTIPY_CLIENT_SECRET = "d1de73d2fe114746ac712b249594e6d8"
SPOTIPY_REDIRECT_URL = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri="http://example.com", client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, show_dialog=True, cache_path="token.txt"))
user_id = sp.current_user()['id']
date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
print("Please wait...")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=URL)
soup = BeautifulSoup(response.text, 'html.parser')

song_lst = [song.get_text().strip() for song in soup.select(selector='li ul li h3')]
year = date.split('-')[0]
song_uris = []

for song in song_lst:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does'nt exist in spotify, skipped.")

playlist = sp.user_playlist_create(user_id, f"{year} Billboard 100", public=False, description=f'Collection of all the songs from year {year}.')
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)

print("Created Successfully.")
