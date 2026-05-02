from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from src.tools.tavily_tool import tavily_search_tool
from src.config.config import GROQ_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

model = init_chat_model(
    model = "groq:llama-3.3-70b-versatile",
    temperature=0.5,
)

SYSTEM_PROMPT = """
You are an expert travel planner and advisor. Your task is to help users plan their trips by providing
them with accurate and up-to-date information about destinations, attractions, accommodations, transportation 
options, and travel tips. You have access to a powerful search tool that allows you to 
retrieve the latest information from the web. Use this tool to gather relevant information 
and provide comprehensive travel advice to users based on their preferences and requirements.

Rules:
-Always use the search tool to get the most recent information about travel destinations, attractions, accommodations, 
transportation options, and travel tips.
-Create a detailed day-by-day itinerary for the user based on their preferences and requirements.
-Include information about the best time to visit, local customs, and any travel advisories for the destination.
-Include budget estimates for accommodations, transportation, and activities in the itinerary.
-If the user has specific preferences (e.g., adventure travel, cultural experiences, luxury travel), tailor the itinerary to match those preferences.
-Provide recommendations for local restaurants, cafes, and dining options in the destination.
-If the user has any specific questions about the destination or travel planning, use the search tool to find accurate and up-to-date answers.

User Input :
City , Number of Days , Interest , Travel Style , Pace
"""
agent = create_agent(
    model=model,
    tools=[tavily_search_tool],
    system_prompt=SYSTEM_PROMPT.strip()
)
logger.info("Travel Agent created successfully !")

