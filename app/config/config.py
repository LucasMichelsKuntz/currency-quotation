from dotenv import load_dotenv
import os

load_dotenv()

DOLLAR_URL = os.getenv("DOLLAR_URL", "http://localhost:3000/cotacao/dolar" )
EURO_URL = os.getenv("EURO_URL", "http://localhost:3000/cotacao/euro")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
