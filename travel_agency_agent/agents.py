from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


groq_api_key = os.environ["GROQ_API_KEY"]
# groq_api_key = st.secrets["GROQ_API_KEY"]

# tools
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model="openai/gpt-3.5-turbo", max_tokens=4000, temperature=0.2
        )
        self.groq = ChatGroq(
            temperature=0, groq_api_key=groq_api_key, model="groq/llama3-8b-8192"
        )

        # Instantiate the tools
        # self.search_tool = SearchTools().search_internet
        self.calculator_tool = CalculatorTools().calculate

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                """Expert in travel planning and logistics. 
                I have decades of expereince making travel iteneraries.
                """
            ),
            goal=dedent("""
                        Create a 7-day travel itinerary with detailed per-day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                """Expert at analyzing travel data to pick ideal destinations"""
            ),
            goal=dedent(
                """Select the best cities based on weather, season, prices, and traveler interests"""
            ),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("""Knowledgeable local guide with extensive information
        about the city, it's attractions and customs"""),
            goal=dedent("""Provide the BEST insights about the selected city"""),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
