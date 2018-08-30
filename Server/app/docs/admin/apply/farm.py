from app.docs import jwt_header

GET_APPLY = {
    'tags': ['[ADMIN] 계정 정보'],
    'description': 'applicant room inform activity',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': '신청한 양식장의 정보를 불러옵니다.',
            'examples': {
                '': {
                    'name': '',
                    'phone_num': '',
                    'start_day': '',
                    'end_day': '',
                    'addition Inform': '',
                    'rooms': [{
                        'code': '',
                        'name'
                    }]
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
