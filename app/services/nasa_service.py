import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get NASA API key from environment variables (or use DEMO_KEY)
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

def fetch_land_use():
    """
    Simulates fetching land use data from NASA.
    Replace with real API calls later.
    """
    # Example placeholder data
    return {
        "city": "Douala",
        "land_use_change": "Urban expansion detected in NW sector",
        "source": "Simulated NASA API"
    }