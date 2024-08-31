from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    # Extract the video ID from the URL
    if "youtu.be" in video_url:
        video_id = video_url.split("/")[-1]
    elif "watch?v=" in video_url:
        video_id = video_url.split("=")[-1]
    else:
        video_id = video_url

    try:
        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Combine the transcript lines into a single string
        transcript_text = '\n'.join([line['text'] for line in transcript])
        return transcript_text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage

# LEX podcast
# video_url = 'https://www.youtube.com/watch?v=lOzDz8maa7s'
# video_url = 'https://www.youtube.com/watch?v=0cn3VBjfN8g'
video_url = 'https://www.youtube.com/watch?v=Dc99-zTMyMg'
# just-testing-ai-agents
transcript = get_transcript(video_url)
print(transcript)
