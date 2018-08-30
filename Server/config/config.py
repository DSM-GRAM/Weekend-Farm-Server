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

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': None,
        'port': None,
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
                'name': '[Admin] 계정 관리',
                'description': '관리자 계정 관련 관리 API'
            },
            {
                'name': '[Admin] 계정 정보',
                'description': '관리자 계정의 정보를 보내주는 API'
            },
            {
                'name': '[Admin] Farm',
                'description': '관리자 계정에서 양식장 관련 데이터 처리 API'
            }
        ]
    }

