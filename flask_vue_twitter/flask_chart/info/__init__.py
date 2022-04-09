from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import config_dict
from redis import StrictRedis
from config import config_dict, Config
import pymongo

mongo_store = pymongo.MongoClient(host=Config.MONGODB_HOST, port=Config.MONGODB_PORT)
mongo_db = mongo_store.twitter


db = SQLAlchemy()
redis_store = StrictRedis(
    host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG)
file_log_handler = RotatingFileHandler(
    "logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
formatter = logging.Formatter(
    '%(levelname)s %(filename)s:%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    Session(app)
    db.init_app(app)

    from info.modules.views import news_blue
    from info.api.chart import chart_print
    app.register_blueprint(news_blue)
    app.register_blueprint(chart_print, url_prefix='/api/v1.0')
    return app



