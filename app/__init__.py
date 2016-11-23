from flask import Flask
from src.build import clegs_ext

app = Flask(__name__)
from app import views
