from rq import get_current_job
from app.models import URL
import requests
from app import Create_app

app = Create_app()
app.app_context().push()


def get_count_words():
    try:
        job = get_current_job()
        print('starting task')
        if job:
            print(job)
            u = URL()
            url_obj = URL.query.filter_by(crwalled=False)
            for url in url_obj:
                resp = requests.get(url.url)
                total_words = len(resp.text.split())
                u.update_total_words(url.id, total_words)
        print('task ended')
    except Exception as exception:
        print('[Error in Tasks:]', exception)
    return False
