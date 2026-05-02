from langchain_community.utilities  import GoogleSerperAPIWrapper
from src.config.config import SERPER_API_KEY
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

def google_serper_search_tool(query : str) -> str:
    try:
        if not SERPER_API_KEY:
            raise ValueError("SERPER_API_KEY is not set in the environment variables")

        search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)
        return search.run(query)
    except Exception as e:
        raise CustomException("Error in google_serper_search_tool", e)
    

logger.info("Google Serper Search Tool is ready to use !")