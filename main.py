from podcast_summarizer_agent import PodcastSummarizerCrew
import streamlit as st

st.set_page_config(page_title="Podcast Summary App", layout="centered")

def run():
    st.title("Podcast Summary App")

    podcast_url = st.text_input("Enter the YouTube URL of podcast you want to summarize")
    slack_channel = st.text_input("Enter the Slack channel name")
    # notion_page = st.text_input("Enter the Notion page you want to write the summary into")

    if st.button("Summarize Podcast"):
        if podcast_url and slack_channel:
            inputs = {
                'youtube_url': podcast_url,
                'slack_channel': slack_channel
            }
            result = PodcastSummarizerCrew().crew().kickoff(inputs=inputs)
            st.write(result)
        else:
            st.write("podcast_url or slack channel is empty")

        # if podcast_url and notion_page:
        #     inputs = {
        #         'youtube_url': podcast_url,
        #         'notion_page': notion_page
        #     }
        #     result = PodcastSummarizerCrew().crew().kickoff(inputs=inputs)
        #     st.write(result)
        # else:
        #     st.write("podcast_url or notion page is empty")

if __name__ == "__main__":
    run()