from langchain_tavily import TavilySearch
from src.config.config import TAVILY_API_KEY
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

def tavily_search_tool(query : str) -> str:
    """
    Search the web using Tavily Search API to get up to date travel information 
    and return the results as a string.
    """
    try:
        if not TAVILY_API_KEY:
            raise ValueError("Tavily API key is not set in the environment variables")
        tavily_search = TavilySearch(
            max_results=5,
            topic="general",
            tavily_api_key=TAVILY_API_KEY
        )

        return tavily_search.invoke({"query" : query })
    
    except Exception as e:
        raise CustomException("Error in tavily_search_tool", e)

logger.info("Tavily Search Tool is ready to use !")