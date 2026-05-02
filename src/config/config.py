import os
from dotenv import load_dotenv
from src.utils.logger import get_logger

load_dotenv()

logger= get_logger(__name__)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
#SERPER_API_KEY = os.getenv("SERPER_API_KEY")

logger.info("Configuration loaded successfully !")
