from flask import current_app
from app import db
from redis import Redis
import rq


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), index=True, unique=True)
    crwalled = db.Column(db.Boolean, default=False)
    total_words = db.Column(db.Integer, default=0)

    def create_entry(self, url, total_words):
        try:
            u = URL(url=url, total_words=total_words, crwalled=True)
            db.session.add(u)
            db.session.commit()
            return True
        except Exception as exception:
            print('[Error in create entry model: ]', exception)
        return False

    def launch_task(self, url):
        try:
            queue = rq.Queue('webpage_reader-tasks', connection=Redis.from_url('redis://'))
            queue.enqueue('app.tasks.save_url', url)
            return True
        except Exception as exception:
            print('[Error in launch task: ]', exception)
        return False

    def __repr__(self):
        return '<URL {}>'.format(self.url)