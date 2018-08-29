SIGNUP_POST = {
    'tags': ['[USER] 계정 생성'],
    'description': 'USER 계정을 생성하는 API',
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
            'name': 'pw_re',
            'description': '생성할 유저 비밀번호와 똑같은 비밀번호 입력',
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
            'name': 'phone_num',
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
        '406': {
            'description': '비밀번호와 비밀번호 재확인이 다름'
        },
        '409': {
            'description': '중복된 ID',
        }
    }
}
