import socket


class Config:
    SERVICE_NAME = 'Weekend-Farm'

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
    DEBUG = True

    SECRET_KEY = 'd7g98afvi32h423f0202kkvbs82'

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
            # Admin ----
            {
                'name': '',
                'description': ''
            },
            # -------------------------------

            # User ----
            {
                'name': '',
                'description': ''
            },
            {
                'name': '',
                'description': ''
            }
            # -------------------------------
        ]
    }
