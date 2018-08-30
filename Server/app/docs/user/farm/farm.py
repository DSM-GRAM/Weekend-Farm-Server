from app.docs import jwt_header

SEARCH_FARM = {
    'tags': ['[User] Farm'],
    'description': '주소로 어떤 시에 어떤 양식장이 존재하는지 정보 줌.',
    'parameters': [
        jwt_header,
        {
            'name': 'donum',
            'description': '도',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '',
            'examples': {
                '': [{
                    'farm_name': '승용이네 양식장',
                    'farm_phone_number': '010-1234-5678',
                    'farm_address': '전북대학교',
                    'farm_details': '많은 관심 부탁드려요'
                },
                    {
                    'farm_name': '진우네 양식장',
                    'farm_phone_number': '010-1235-5678',
                    'farm_address': '전북대학교',
                    'farm_details': '많은 사랑 부탁드려요'
                }]
            }
        },
        '204': {
            'description': '해당 주소에 양식장 없음',
        }
    }
}

