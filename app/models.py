from flask import current_app
from app import db
import redis
import rq


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), index=True, unique=True)
    crwalled = db.Column(db.Boolean, default=False)
    total_words = db.Column(db.Integer, default=0)
    tasks = db.relationship('Tasks', backref='user', lazy='dynamic')

    def create_entry(self, url, total_words):
        try:
            u = URL(url=url, total_words=total_words, crwalled=True)
            db.session.add(u)
            db.session.commit()
            return True
        except Exception as exception:
            print('[Error in create entry model: ]', exception)
        return False

    # def update_total_words(self, id, total_words):
    #     u = URL.query.filter_by(id=id).update(dict(total_words=total_words))
    #     db.session.commit()

    def launch_task(self, name, description):
        try:
            rq_job = current_app.task_queue.enqueue('app.tasks.' + name, self.id)
            task = Tasks(id=rq_job.get_id(), name=name, description=description,
                         user=self)
            db.session.add(task)
            return task
        except Exception as exception:
            print('[Error in launch task: ]', exception)
        return False

    def __repr__(self):
        return '<URL {}>'.format(self.url)


class Tasks(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(128))
    url_id = db.Column(db.Integer, db.ForeignKey('URL.id'))
    complete = db.Column(db.Boolean, default=False)

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', 0) if job is not None else 100
