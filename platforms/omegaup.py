import requests
from bs4 import BeautifulSoup
import json

def get_omegaup_solved(username):
    url = f"https://omegaup.com/profile/{username}/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        script_tag = soup.find('script', {'type': 'text/json', 'id': 'payload'})

        if not script_tag:
            return -1

        data = json.loads(script_tag.string)
        return data["profile"]["rankinfo"]["problems_solved"]

    except Exception as e:
        return -1
