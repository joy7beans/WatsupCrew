from crewai import Agent
from langchain_groq import ChatGroq
from config import GROQ_API_KEY,SERPER_API_KEY,OPENAI_API_KEY
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool,  SeleniumScrapingTool
import os

os.environ["SERPER_API_KEY"] = SERPER_API_KEY

custom_GPT_model = ChatOpenAI(model_name="gpt-4-turbo",api_key=OPENAI_API_KEY)

custom_model = ChatGroq(
    model = "Llama3-70b-8192",
    api_key=GROQ_API_KEY
)

# Initialize the SerperDevTool
serper_search_tool = SerperDevTool(search_url="https://google.serper.dev/news", n_results=2)
scraper = SeleniumScrapingTool()

class CrewAgents():

    def searcher(self):
        return Agent(
            role='searcher',
            goal='Search the web for weblinks on the specific topic of interest and summarize it.',
            backstory='Experienced web searcher with a curious mind that seeks latest information from the web.',
            verbose=True,
            llm=custom_GPT_model,
            tools = [serper_search_tool]
        )
    
    def editor(self):
        return Agent(
            role='analyst',
            goal='Summarize all the results. ',
            backstory='Experienced analyst who can understand multple references and analyze content to summarize key ideas.',
            verbose=True,
            llm=custom_GPT_model
        )