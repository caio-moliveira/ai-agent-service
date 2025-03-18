import streamlit as st
from main import TripCrew

st.title("Welcome to Trip Planner Crew")

with st.sidebar:
    st.header("Enter Your Trip Details")
    topic = "Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips."
    origin = st.text_input("From where will you be traveling from?")
    cities = st.text_input(
        "What are the cities options you are interested in visiting?"
    )
    date_range = st.text_input(
        "What is the date range you are interested in traveling?"
    )
    interests = st.text_input("What are some of your high level interests and hobbies?")

if st.button("Run Research"):
    if not topic or not origin or not cities or not date_range or not interests:
        st.error("Please fill all the fields.")
    else:
        # inputs = f"Research Topic: {topic}\nOrigin: {origin}\City: {cities}\date_range: {date_range}\nInterests: {interests}"
        # inputs = {topic, origin, cities, date_range, interests}
        research_crew = TripCrew(origin, cities, date_range, interests)
        result = research_crew.run()
        st.subheader("Here is you Trip Plan:")
        st.write(result)
