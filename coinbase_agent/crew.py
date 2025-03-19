import streamlit as st
import yaml
import os
from crewai import Agent, Task, Crew
from tools.get_crypto_price import GetCryptoPriceTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set required environment variables for CrewAI
os.environ["OPENAI_API_MODEL"] = "gpt-4o-mini"

# Define file paths for YAML config
files = {
    "agents": "coinbase_agent/config/agents.yaml",
    "tasks": "coinbase_agent/config/tasks.yaml",
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, "r") as file:
        configs[config_type] = yaml.safe_load(file)

agents_config = configs["agents"]
tasks_config = configs["tasks"]

# Instantiate the tool
crypto_price_tool = GetCryptoPriceTool()

# Create agent dynamically
crypto_analyst = Agent(
    config=agents_config["crypto_analyst"], tools=[crypto_price_tool]
)

# Streamlit UI
st.set_page_config(page_title="Crypto Price Checker", page_icon="📈")

st.title("📈 Crypto Price Checker")
st.write("Enter a cryptocurrency and a fiat currency to get the latest price.")

# User Inputs
crypto = st.text_input("Enter Cryptocurrency Symbol (e.g., BTC, ETH)").upper()
currency = st.text_input("Enter Fiat Currency Symbol (e.g., USD, EUR, GBP)").upper()

# Fetch Price Button
if st.button("Get Price"):
    with st.spinner("Fetching price..."):
        # Create task dynamically with interpolation
        fetch_crypto_price = Task(
            config=tasks_config["fetch_crypto_price"],
            agent=crypto_analyst,
            output_file="coinbase_agent/results/report.md",
        )

        # Create and run the Crew
        crew = Crew(agents=[crypto_analyst], tasks=[fetch_crypto_price], verbose=False)

        # Provide user inputs dynamically
        inputs = {"crypto": crypto, "currency": currency}

        # Run the CrewAI process
        result = crew.kickoff(inputs=inputs)

        # Display Result
        st.success("✅ Latest Price Retrieved!")
        st.write(result)
