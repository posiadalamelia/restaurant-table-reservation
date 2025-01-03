from flask import Flask
from redis import Redis
import os

app = Flask(__name__) # Flask appliaction's object
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key_here')
app.config['REDIS_HOST'] = os.getenv('REDIS_HOST', 'redis')
app.config['REDIS_PORT'] = os.getenv('REDIS_PORT', 6379)

redis_client = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], decode_responses=True) # responses as string, not bytes

from app import routes

