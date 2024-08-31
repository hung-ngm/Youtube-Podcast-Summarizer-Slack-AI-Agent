from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.audio_transcriber import audio_transcriber_tool
from tools.composio_slack import composio_slack_tool
from tools.composio_notion import composio_notion_tool
import os
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class PodcastSummarizerCrew:
    "Podcast summarizer and slack mesenger Crew"
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    audio_tool = [audio_transcriber_tool]
    slack_tool = composio_slack_tool()
    notion_tool = composio_notion_tool()
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
    llm_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # llm_model = ChatAnthropic(
    #     model="claude-3-5-sonnet-20240620",
    #     temperature=0,
    #     # max_tokens=1024,
    #     # timeout=None,
    #     # max_retries=2,
    #     # other params...
    # )
    # llm_model =  AzureChatOpenAI(openai_api_version=os.getenv("AZURE_OPENAI_VERSION", "2023-07-01-preview"),
    #         azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt4chat"),
    #         azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "https://gpt-4-trails.openai.azure.com/"),
    #         api_key=os.getenv("AZURE_OPENAI_KEY"))


    @agent
    def summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['transcriber_summarizer'],
            tools = self.audio_tool,
            verbose = True,
            llm = self.llm_model,
            allow_delegation = False,
        )

    @agent
    def slack_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['slack_messenger'],
            tools = self.slack_tool,
            verbose = True,
            llm = self.llm_model,
        )

    # @agent
    # def notion_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['notion_writer'],
    #         tools=self.notion_tool,
    #         verbose=True,
    #         llm=self.llm_model,
    #     )

    @task
    def generate_summary(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_podcast_task'],
            tools=self.audio_tool,
            agent=self.summary_agent(),
        )

    @task
    def send_message(self) -> Task:
        return Task(
            config=self.tasks_config['send_message_to_slack_task'],
            tools=self.slack_tool,
            agent=self.slack_agent()
        )
    
    # @task
    # def write_to_notion(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['write_summary_to_notion_task'],
    #         tools=self.notion_tool,
    #         agent=self.notion_agent()
    #     )

    @crew
    def crew(self) -> Crew:
        """Create a crew for the Podcast Summarizer"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
        )
