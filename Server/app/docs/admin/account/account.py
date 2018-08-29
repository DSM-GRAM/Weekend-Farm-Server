from app.docs import jwt_header

ADMIN_ADD_ADDITION = {
    'tags': ['[ADMIN] 계정 정보 작성'],
    'description': '의 정보를 작성하고 저장합니다.',
    'parameters': [
        jwt_header,
        {
            'name': 'name',
            'description': '양식장 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'phone_num',
            'description': '양식장 전화번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'address',
            'description': '양식장 주소',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'addition',
            'description': '부가 정보',
            'in': 'json',
            'type': 'str',
            'required': False
        },
    ],
    'responses': {
        '201': {
            'description': '정보 작성 완료',
        },
        '403': {
            'description': '권한 없음',
        },
        '406': {
            'description': '잘못된 요청',
        }
    }
}
