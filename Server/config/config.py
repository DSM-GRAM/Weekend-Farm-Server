import socket
import os


class Config:
    SERVICE_NAME = 'Weekend-Farm'

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
    DEBUG = True

    SECRET_KEY = os.getenv('SECRET_KEY')

    RUN_SETTINGS = {
        "host": HOST,
        "port": PORT,
        "debug": DEBUG
    }

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': '/docs',
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': 'Weekend Farm'
        },
        'basePath': '/'
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            # --- Admin
            {
                'name': '[Admin] 계정',
                'description': '관리자 계정 관련 API'
            },
            {
                'name': '[Admin] 모름',
                'description': '모름'
            },
        ]
    }

