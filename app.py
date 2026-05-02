import warnings
import streamlit as st

from dotenv import load_dotenv
from src.core.planner import TravelPlanner
from src.utils.logger import get_logger
warnings.filterwarnings("ignore")

load_dotenv()
logger = get_logger(__name__)

st.set_page_config(page_title="TravellerAI - Your Personal Travel Planner", page_icon=":airplane:", layout="wide")
st.title("🧳 Welcome to TravellerAI : Your Personal Travel Planner")

with st.form("planner_form"):
    city = st.text_input("Enter the destination 📍 city:")
    days = st.number_input("Number of days 🗓️ for the trip:", min_value=1, max_value=30, value=5)
    interests = st.text_input("Enter your interests (comma separated) 🎯 e.g. culture, food, nature:")
    style = st.selectbox("Select your travel style 🧭 " ,
                         ["Budget" , "Luxury" , "Adventure" , "Cultural" , "Relaxation"])
    pace = st.selectbox("🚶🏻 Select your prefered pace:" , 
                        ["Balanced" , "Fast-Paced" , "Leisure"])
    month = st.selectbox("Select the month of travel 📅 (optional):" , 
                         ["Any", "January", "February", "March", "April", "May", "June", 
                          "July", "August", "September", "October", "November", "December"])
    submitted = st.form_submit_button("Plan My Trip 🧳")


if submitted :
    if city and interests:
        planner = TravelPlanner()
        iternary = planner.create_itinerary(
            city=city,
            days=days,
            interests=[interest.strip() for interest in interests.split(",")],
            style=style,
            pace=pace,
            month=None if month == "Any" else month
        )
        st.subheader("Your Personalized Travel Itinerary 🗺️")
        st.markdown(iternary)
        
        logger.info("Response generated successfully for the user !")
        
    else:
        st.warning("🚧 Please enter both the destination city and your interests to generate a travel itinerary.")
    