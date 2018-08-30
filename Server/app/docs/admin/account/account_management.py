from app.docs import jwt_header

ADMIN_ADD_INFORM = {
    'tags': ['[Admin] 계정'],
    'description': 'Admin의 정보를 작성하고 저장합니다. (Add Admin Inform)',
    'parameters': [
        jwt_header,
        {
            'name': 'farm_name',
            'description': '양식장 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'farm_phone_number',
            'description': '양식장 전화번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'farm_address',
            'description': '양식장 주소',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'additional',
            'description': '부가 정보',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'room_name',
            'description': '사용 가능 양식장의 이름',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'room_cost',
            'description': '사용 가능 양식장의 월 별 가격',
            'in': 'json',
            'type': 'int',
            'required': False
        },
        {
            'name': 'room_fish',
            'description': '사용 가능 양식장의 물고기 마리 수',
            'in': 'json',
            'type': 'int',
            'required': False
        },
        {
            'name': 'room_Temperature',
            'description': '사용 가능 양식장의 이름',
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

RETURN_ADMIN_ADD_INFORM = {

}
