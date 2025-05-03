import requests
import re
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_atcoder_solved(username, token):
    contest_types = ['algo', 'heuristic']
    contest_names = set()

    for contest_type in contest_types:
        url = f"https://atcoder.jp/users/{username}/history?contestType={contest_type}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.6',
            'Referer': f'https://atcoder.jp/users/{username}',
        }

        cookies = {}
        if token:
            cookies['REVEL_SESSION'] = token

        try:
            response = requests.get(url, headers=headers, cookies=cookies)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=re.compile(r'/contests/[^/]+/submissions\?f\.User=' + username)):
                contest_name = link['href'].split('/')[2]
                contest_names.add(contest_name)
        except requests.RequestException:
            continue

    if not contest_names:
        return -1

    unique_problems = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.6',
    }

    for contest_name in contest_names:
        time.sleep(0.5)
        url = f"https://atcoder.jp/contests/{contest_name}/submissions?f.User={username}"
        cookies = {}
        if token:
            cookies['REVEL_SESSION'] = token

        try:
            response = requests.get(url, headers=headers, cookies=cookies)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            for row in soup.select('tbody tr'):
                ac_span = row.select_one('span.label-success[title="Accepted"]')
                if not ac_span:
                    continue

                problem_link = row.select_one('td:nth-of-type(2) a')
                if problem_link:
                    problem_name = problem_link.text.strip()
                    unique_problems.add(problem_name)
        except requests.RequestException:
            continue

    return len(unique_problems) if unique_problems else -1
