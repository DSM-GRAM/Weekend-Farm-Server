USER_SIGNUP_POST = {
    'tags': ['[User] 계정'],
    'description': 'Admin 계정을 생성하는 API',
    'parameters': [
        {
            'name': 'id',
            'description': '생성할 유저 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '생성할 유저 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '생성할 유저 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'phone_number',
            'description': '생성할 유저 계정의 전화번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '가입 성공'
        },
        '409': {
            'description': '중복된 ID',
        }
    }
}
