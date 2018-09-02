import socket
import os
from datetime import timedelta


class Config:
    SERVICE_NAME = 'Weekend-Farm'

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
    DEBUG = True

    SECRET_KEY = 'dopsdfjdfob8d2230tvnmk'

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)

    RUN_SETTINGS = {
        "host": HOST,
        "port": PORT,
        "debug": DEBUG
    }

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': None,
        'port': None,
        'username': os.getenv('MONGO_ID'),
        'password': os.getenv('MONGO_PW')
    }
