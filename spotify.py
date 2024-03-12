import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "e97cf6bc063742d8b6f931524b0bc22b"
SPOTIPY_CLIENT_SECRET = "d1de73d2fe114746ac712b249594e6d8"
SPOTIPY_REDIRECT_URL = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri="http://example.com", client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, show_dialog=True, cache_path="token.txt", username="31x56arm22uzldj7zc7fynmb3cri",))


user_id = sp.current_user()["id"]
