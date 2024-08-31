# import yt_dlp
# import os

# # Set up the save path and URL
# SAVE_PATH = "/Users/hungng/Documents/AI/pet-projects/composio-podcast-summarizer-agent"
# URL = "https://www.youtube.com/watch?v=jvqFAi7vkBc"

# # Configure yt-dlp options
# ydl_opts = {
#     'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
#     'outtmpl': os.path.join(SAVE_PATH, 'videoFilename.%(ext)s'),
# }

# # Create a yt-dlp object and download the video
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     try:
#         info = ydl.extract_info(URL, download=True)
#         print(f"Downloaded: {info['title']}")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# # Check if the file was downloaded
# expected_file_path = os.path.join(SAVE_PATH, 'videoFilename.mp4')
# if os.path.exists(expected_file_path):
#     print(f"File successfully downloaded to: {expected_file_path}")
#     print(f"File size: {os.path.getsize(expected_file_path) / (1024 * 1024):.2f} MB")
# else:
#     print("File download failed or saved with a different name.")

# import yt_dlp
# import os

# # Set up the save path and URL
# SAVE_PATH = "/Users/hungng/Documents/AI/pet-projects/composio-podcast-summarizer-agent"
# URL = "https://www.youtube.com/watch?v=jvqFAi7vkBc"

# # Configure yt-dlp options for audio-only download in mp3 format
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
#     'outtmpl': os.path.join(SAVE_PATH, 'audioFilename.%(ext)s'),
# }

# # Create a yt-dlp object and download the audio
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     try:
#         info = ydl.extract_info(URL, download=True)
#         print(f"Downloaded audio from: {info['title']}")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# # Check if the file was downloaded
# expected_file_path = os.path.join(SAVE_PATH, 'audioFilename.mp3')
# if os.path.exists(expected_file_path):
#     print(f"Audio file successfully downloaded to: {expected_file_path}")
#     print(f"File size: {os.path.getsize(expected_file_path) / (1024 * 1024):.2f} MB")
# else:
#     print("Audio file download failed or saved with a different name.")

import yt_dlp
import os
import whisper

# Set up the save path and URL
SAVE_PATH = "/Users/hungng/Documents/AI/pet-projects/composio-podcast-summarizer-agent"
# URL = "https://www.youtube.com/watch?v=8wvyBN-fEsE"
URL = "https://www.youtube.com/watch?v=J7aiEwp1x9k"

# Configure yt-dlp options for audio-only download
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(SAVE_PATH, 'audioFilename.%(ext)s'),
}

# Function to download audio
def download_audio(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=True)
            print(f"Downloaded audio from: {info['title']}")
            return os.path.join(SAVE_PATH, 'audioFilename.mp3')
        except Exception as e:
            print(f"An error occurred during download: {str(e)}")
            return None

# Function to transcribe audio
def transcribe_audio(audio_path):
    try:
        print("Loading Whisper model...")
        model = whisper.load_model("small")
        print("Transcribing audio...")
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"An error occurred during transcription: {str(e)}")
        return None

# Main execution
if __name__ == "__main__":
    # Download audio
    audio_file_path = download_audio(URL)
    
    if audio_file_path and os.path.exists(audio_file_path):
        print(f"Audio file successfully downloaded to: {audio_file_path}")
        print(f"File size: {os.path.getsize(audio_file_path) / (1024 * 1024):.2f} MB")
        
        # Transcribe audio
        transcription = transcribe_audio(audio_file_path)
        
        if transcription:
            print("\nTranscription:")
            print(transcription)
        
        # Optionally, remove the audio file after transcription
        # os.remove(audio_file_path)
    else:
        print("Audio file download failed or file not found.")