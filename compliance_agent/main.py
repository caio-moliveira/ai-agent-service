from crew import ComplianceCrew


def run_compliance_assistant(question: str):
    """
    Runs the Compliance AI Assistant with the given question.

    Args:
        question (str): The compliance question to be answered.

    Returns:
        str: The response from the AI compliance agent.
    """
    if not question.strip():
        return "⚠️ Please enter a valid question."

    # Initialize the ComplianceCrew
    crew_instance = ComplianceCrew()

    # Run the AI Compliance Assistant
    result = crew_instance.crew().kickoff(inputs={"question": question})

    return result
