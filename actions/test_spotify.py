import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import whisper
import os
import requests

# Set up Spotify API credentials
client_id = 'YOUR SPOTIFY CLIENT ID'
client_secret = 'YOUR SPOTIFY CLIENT SECRET'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

# Get the podcast episode URL
episode_url = 'https://open.spotify.com/episode/4eOOhNrca333tLMVaGLZjT'

# Extract the show
show = sp.show("https://open.spotify.com/show/6aB0v6amo3a8hgTCjlTlvh")

episodes = show['episodes']['items']

# Download each episode
episode = episodes[0]
print(episode)
# episode_name = episode['name']
# audio_url = episode['audio_preview_url']
# if audio_url:
#     response = requests.get(audio_url)
#     with open(f"{episode_name}.mp3", "wb") as file:
#         file.write(response.content)
#     print(f"Downloaded {episode_name}")
# else:
#     print(f"No audio preview available for {episode_name}")

# Download the episode
# episode = sp.episode(episode_url)
# audio_url = episode['audio_preview_url']

# # Download the audio file
# audio_file = 'podcast_episode.mp3'
# os.system(f"wget -O {audio_file} {audio_url}")

# # Transcribe the audio using Whisper
# whisper_model = whisper.load_model("small")
# result = whisper_model.transcribe(audio_file)

# # Print the transcription
# print(result["text"])
