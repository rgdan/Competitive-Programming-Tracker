import requests
from bs4 import BeautifulSoup

def get_codeforces_solved(username):
    url = f"https://codeforces.com/profile/{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return -1

    soup = BeautifulSoup(response.text, 'html.parser')
    counters = soup.select('div._UserActivityFrame_counter')

    for counter in counters:
        desc = counter.select_one('div._UserActivityFrame_counterDescription')
        if desc and "solved for all time" in desc.text:
            value_div = counter.select_one('div._UserActivityFrame_counterValue')
            if value_div:
                try:
                    number_text = value_div.text.strip().split()[0]
                    return int(number_text)
                except (ValueError, IndexError):
                    return -1

    return -1
