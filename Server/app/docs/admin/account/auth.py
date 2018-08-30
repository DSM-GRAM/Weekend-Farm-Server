from app.docs import SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN

ADMIN_AUTH_POST = {
    'tags': ['[Admin] 계정'],
    'description': 'ADMIN 로그인을 하고, ACCESS_TOKEN 과 REFRESH_TOKEN 을 발급함.',
    'parameters': [
        {
            'name': 'id',
            'description': 'ADMIN ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': 'ADMIN PW',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': '로그인 섣공 및 token 생성',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN,
                    'refreshToken': SAMPLE_REFRESH_TOKEN
                }
            }
        },
        '401': {
            'description': '로그인 실패'
        }
    }
}
