from rq import get_current_job
from app.models import URL
import requests


def get_count_words(url):
    total_words = 0
    try:
        print('starting task')
        resp = requests.get(url)
        total_words = len(resp.text.split())
        print('task ended')
    except Exception as exception:
        print('[Error in get count words Tasks:]', exception)
    return total_words


def save_url(url):
    try:
        total_words = get_count_words(url)
        URL().create_entry(url, total_words)
        return True
    except Exception as exception:
        print('[Error in save url tasks:]', exception)
    return False
