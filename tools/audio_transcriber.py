# from crewai_tools import tool
# from pytube import YouTube
# import whisper

# @tool("Audio Transcribe Tool")
# def audio_transcriber_tool(url: str) -> str:
#     """
#     Extracts audio and transcribe the audio from a YouTube video given its URL and summarizes it.

#     Parameters:
#     - url (str): The URL of the YouTube video from which audio will be extracted.

#     Returns:
#     str: A string containing:
#         - The summarized version of the Transcribed Youtube URL
#     """
#     yt = YouTube(url)
#     video = yt.streams.filter(only_audio=True).first()
#     out_file = video.download()
#     video_details = {
#         "name": yt.title,
#     }
#     whisper_model = whisper.load_model("small")
#     result = whisper_model.transcribe(out_file)
#     return result["text"]

# from crewai_tools import tool
# import yt_dlp
# import whisper
# import os

# @tool("Audio Transcribe Tool")
# def audio_transcriber_tool(url: str, save_path: str = "/tmp") -> str:
#     """
#     Extracts audio and transcribes the audio from a YouTube video given its URL.

#     Parameters:
#     - url (str): The URL of the YouTube video from which audio will be extracted.
#     - save_path (str): The directory where the audio file will be temporarily saved. Defaults to "/tmp".

#     Returns:
#     str: A string containing the transcribed text from the YouTube video.
#     """
#     # Configure yt-dlp options for audio-only download
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#         'outtmpl': os.path.join(save_path, 'audioFilename.%(ext)s'),
#     }

#     try:
#         # Download audio
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)
#             video_details = {
#                 "name": info['title'],
#             }
        
#         # Path to the downloaded audio file
#         audio_file = os.path.join(save_path, 'audioFilename.mp3')

#         print(f"Audio file downloaded to: {audio_file}")
#         print(f"File size: {os.path.getsize(audio_file) / (1024 * 1024):.2f} MB")

#         # Transcribe audio
#         print("Loading Whisper model...")
#         whisper_model = whisper.load_model("small")
#         print("Transcribing audio...")
#         result = whisper_model.transcribe(audio_file)

#         # Clean up: remove the temporary audio file
#         os.remove(audio_file)

#         return result["text"]

#     except Exception as e:
#         return f"An error occurred: {str(e)}"


from crewai_tools import tool
from youtube_transcript_api import YouTubeTranscriptApi

@tool("Audio Transcribe Tool")
def audio_transcriber_tool(url: str) -> str:
    """
    Transcribes the audio from a YouTube video given its URL.

    Parameters:
    - url (str): The URL of the YouTube video to be transcribed.

    Returns:
    str: A string containing the transcribed text from the YouTube video.
    """
    # Extract the video ID from the URL
    if "youtu.be" in url:
        video_id = url.split("/")[-1]
    elif "watch?v=" in url:
        video_id = url.split("=")[-1]
    else:
        video_id = url

    try:
        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Combine the transcript lines into a single string
        transcript_text = '\n'.join([line['text'] for line in transcript])
        return transcript_text
    except Exception as e:
        return f"An error occurred: {e}"