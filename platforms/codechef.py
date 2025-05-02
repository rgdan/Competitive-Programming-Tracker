import requests
from bs4 import BeautifulSoup

def get_codechef_solved(username):
    url = f"https://www.codechef.com/users/{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return -1

    soup = BeautifulSoup(response.text, 'html.parser')
    rating_section = soup.find('section', class_='rating-data-section problems-solved')

    if not rating_section:
        return -1

    problems_solved = 0

    for content_div in rating_section.find_all('div', class_='content'):
        problem_spans = content_div.find_all('span', style=lambda value: value and 'font-size: 12px' in value)
        problems_solved += len(problem_spans)

    return problems_solved if problems_solved > 0 else -1
