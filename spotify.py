import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Konfigurasi API
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'http://localhost:8888/callback' # Pastikan sama dengan di dashboard
scope = "user-modify-playback-state user-read-playback-state"

# Autentikasi
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Contoh: Memutar lagu (memerlukan Spotify Premium)
track_uri = 'spotify:track:4iV5W9uYEdYUVa79Axb7vS'
sp.start_playback(uris=[track_uri])
print("Sedang memutar lagu...")
