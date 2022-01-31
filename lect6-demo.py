import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

params = {
    "q": "gamestop",  # Query keywords
    "api-key": os.getenv("NYT_KEY"),
}

response = requests.get(BASE_URL, params=params)
data = response.json()
print(data)

# Print headlines for first 10 articles returned by search endpoint
for i in range(0, 10):
    print(data["response"]["docs"][i]["headline"]["main"])
