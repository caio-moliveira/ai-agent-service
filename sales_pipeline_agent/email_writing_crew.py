import yaml
import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Set required environment variables for CrewAI
os.environ["OPENAI_API_MODEL"] = "gpt-4o-mini"

# Define file paths for YAML config
files = {
    "email_agents": "sales_pipeline_agent/config/email_engagement_agents.yaml",
    "email_tasks": "sales_pipeline_agent/config/email_engagement_tasks.yaml",
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, "r") as file:
        configs[config_type] = yaml.safe_load(file)

email_agents_config = configs["email_agents"]
email_tasks_config = configs["email_tasks"]


# Creating Agents
email_content_specialist = Agent(
    config=email_agents_config["email_content_specialist"],
)

engagement_strategist = Agent(
    config=email_agents_config["engagement_strategist"],
)

# Creating Tasks
email_drafting = Task(
    config=email_tasks_config["email_drafting"], agent=email_content_specialist
)

engagement_optimization = Task(
    config=email_tasks_config["engagement_optimization"], agent=engagement_strategist
)

# Creating Crew
email_writing_crew = Crew(
    agents=[email_content_specialist, engagement_strategist],
    tasks=[email_drafting, engagement_optimization],
    verbose=True,
)
