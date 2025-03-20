import yaml
import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from sales_pipeline_agent.models import LeadScoringResult

# Load environment variables
load_dotenv()

# Set required environment variables for CrewAI
os.environ["OPENAI_API_MODEL"] = "gpt-4o-mini"

# Define file paths for YAML config
files = {
    "lead_agents": "sales_pipeline_agent/config/lead_qualification_agents.yaml",
    "lead_tasks": "sales_pipeline_agent/config/lead_qualification_tasks.yaml",
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, "r") as file:
        configs[config_type] = yaml.safe_load(file)

lead_agents_config = configs["lead_agents"]
lead_tasks_config = configs["lead_tasks"]


# Crew Agents
lead_data_agent = Agent(
    config=lead_agents_config["lead_data_agent"],
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
)

cultural_fit_agent = Agent(
    config=lead_agents_config["cultural_fit_agent"],
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
)

scoring_validation_agent = Agent(
    config=lead_agents_config["scoring_validation_agent"],
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
)

# Crew tasks

lead_data_task = Task(config=lead_tasks_config["lead_data_task"], agent=lead_data_agent)

cultural_fit_task = Task(
    config=lead_tasks_config["cultural_fit_task"], agent=cultural_fit_agent
)

scoring_validation_task = Task(
    config=lead_tasks_config["scoring_validation_task"],
    agent=scoring_validation_agent,
    context=[lead_data_task, cultural_fit_task],
    output_pydantic=LeadScoringResult,
)


# Crew

lead_scoring_crew = Crew(
    agents=[lead_data_agent, cultural_fit_agent, scoring_validation_agent],
    tasks=[lead_data_task, cultural_fit_task, scoring_validation_task],
    verbose=True,
)
