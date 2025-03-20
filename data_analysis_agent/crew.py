import os
import yaml
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Get the current directory (where main.py is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define file paths
files = {
    "agents": os.path.join(current_dir, "config", "agents.yaml"),
    "tasks": os.path.join(current_dir, "config", "tasks.yaml"),
    "csv": os.path.join(current_dir, "support_tickets_data.csv"),
}

# Set required environment variables for CrewAI
os.environ["OPENAI_API_MODEL"] = "gpt-4o-mini"


# Load YAML configurations
configs = {}
for config_type, file_path in files.items():
    if config_type != "csv":  # Skip CSV file for YAML loading
        try:
            with open(file_path, "r") as file:
                configs[config_type] = yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: Configuration file not found at {file_path}")
            exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {file_path}: {e}")
            exit(1)

agents_config = configs["agents"]
tasks_config = configs["tasks"]

# Initialize CSV tool with absolute path and check if file exists
csv_path = files["csv"]
if not os.path.exists(csv_path):
    print(f"Error: CSV file not found at {csv_path}")
    print(
        "Please ensure 'support_tickets_data.csv' is in the same directory as this script"
    )
    exit(1)

csv_tool = FileReadTool(file_path=csv_path)


def main():
    # Create Agents
    suggestion_generation_agent = Agent(
        config=agents_config["suggestion_generation_agent"], tools=[csv_tool]
    )

    reporting_agent = Agent(config=agents_config["reporting_agent"], tools=[csv_tool])

    chart_generation_agent = Agent(
        config=agents_config["chart_generation_agent"], allow_code_execution=True
    )

    # Create Tasks
    suggestion_generation = Task(
        config=tasks_config["suggestion_generation"], agent=suggestion_generation_agent
    )

    table_generation = Task(
        config=tasks_config["table_generation"], agent=reporting_agent
    )

    chart_generation = Task(
        config=tasks_config["chart_generation"], agent=chart_generation_agent
    )

    final_report_assembly = Task(
        config=tasks_config["final_report_assembly"],
        agent=reporting_agent,
        context=[suggestion_generation, table_generation, chart_generation],
        output_file="data_analysis_agent/support_ticket_report.md",  # Save the final report as Markdown
    )

    # Create and configure Crew
    support_report_crew = Crew(
        agents=[suggestion_generation_agent, reporting_agent, chart_generation_agent],
        tasks=[
            suggestion_generation,
            table_generation,
            chart_generation,
            final_report_assembly,
        ],
        verbose=True,
    )

    # Execute the crew
    print("Starting Crew execution...")
    result = support_report_crew.kickoff()

    # Print the result
    print("\n=== Execution Result ===")
    print(result.raw)


if __name__ == "__main__":
    main()
