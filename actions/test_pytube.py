from pytube import YouTube

SAVE_PATH = "/Users/hungng/Documents/AI/pet-projects/composio-podcast-summarizer-agent"
URL = "https://www.youtube.com/watch?v=jvqFAi7vkBc"
yt = YouTube(URL)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH, 'videoFilename', 'mp4')