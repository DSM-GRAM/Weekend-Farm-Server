from app.docs import jwt_header

USER_ADD_ADDITION = {
    'tags': ['[USER] 계정 정보 작성'],
    'description': 'USER 계정 정보 작성',
    'parameters': [
        jwt_header,
        {
            'name': '',
            'description': '',
            'in': '',
            'type': '',
            'required': None
        }
    ],
    'responses': {
        '200': {
            'description': '',
            'examples': {
                '': {
                    '': ''
                }
            }
        },
        '201': {
            'description': '',
            'examples': {
                '': {
                    '': ''
                }
            }
        }
    }
}
