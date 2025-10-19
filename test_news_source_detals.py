import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the SERP API key from environment variables
SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

# Define the base URL for the SERP API
base_url = "https://serpapi.com/search"

# Set up the search query for "tomato" and "Elon Musk"
params = {
    "q": "tomato elon musk",  # The search query
    "api_key": SERP_API_KEY,  # API key from environment
    "engine": "google"        # Use the Google search engine
}

# Make the GET request to the SERP API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    data = response.json()
    print("Search Results:", data)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Error:", response.text)
