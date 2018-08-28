from flask import Flask

def create_app(_app):
    _app = Flask(__name__)

    return _app