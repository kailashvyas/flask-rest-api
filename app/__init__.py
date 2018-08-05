from flask import Flask
from db import db

app = Flask(__name__)

from app import routes