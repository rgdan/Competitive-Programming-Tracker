import requests
from bs4 import BeautifulSoup

def get_codeforces_solved(username):
    url = f"https://codeforces.com/contests/with/{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return -1

    soup = BeautifulSoup(response.text, 'html.parser')
    total_solved = 0
    submission_links = soup.find_all('a', href=lambda href: href and f'/submissions/{username}/contest/' in href)

    for link in submission_links:
        try:
            count = int(link.text.strip())
            total_solved += count
        except (ValueError, AttributeError):
            continue

    return total_solved if total_solved > 0 else -1

