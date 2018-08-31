from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.models.farm import FarmModel
from app.models.apply import ApplyModel
from app.models.admin import AdminModel
from app.views import BaseResource

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin/apply'


@api.resource('')
class ApplyFromUser(BaseResource):
    @swag_from()
    @jwt_required
    def get(self):
        """
        유저가 보낸 신청을 불러오는 API
        """
        farm = FarmModel.objects(admin=AdminModel.objects(id=get_jwt_identity()).first()).first()
        apply = ApplyModel.objects(farm=farm).all()

        return self.unicode_safe_json_dumps([{
            'farm_name': apply.farm.farm_name,
            'user_phone_number': apply.user.phone_number,
            'applyDate': apply.applyDate,
            'message': apply.message,
            'roominfo': [{
                'itemNum': apply.roominfo.itemNum,
                'itemName': apply.roominfo.itemName,
                'money': apply.money
            }]
        } for apply in apply], 200)
