from flask import Flask
from redis import Redis

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import rq

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def create_app(config_class=Config):
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('webpage_reader-tasks', connection=app.redis)


from app import routes
