import streamlit as st
from main import run_compliance_assistant

st.title("🔎 Pharma Compliance AI Assistant")
st.write(
    "This AI helps you with **ANVISA (Brazil) GMP Compliance** based on RDC 301, RDC 658, and BPF regulations."
)

# Sidebar for user selection
with st.sidebar:
    st.header("Select a Task:")
    task_type = (
        "Answer Compliance Question"  # Since we have only one task, it's pre-selected
    )

    # Input field for user question
    user_input = st.text_area("Enter your compliance question:")

# Run the AI Compliance Assistant when the user clicks the button
if st.button("Run Compliance Check 🚀"):
    if not user_input.strip():
        st.warning("⚠️ Please enter your question before running.")
    else:
        st.write("⏳ Processing your request... Please wait.")

        # ✅ Call the function from main.py
        result = run_compliance_assistant(user_input)

        # Display the AI response
        st.subheader("✅ Compliance AI Response:")
        st.write(result)
