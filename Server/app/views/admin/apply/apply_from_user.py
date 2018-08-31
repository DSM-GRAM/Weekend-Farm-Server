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
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        farm = FarmModel.objects(farm_hostname=admin.name).first()
        apply = ApplyModel.objects(farm_name=farm.farm_name).all()

        return self.unicode_safe_json_dumps([{
            'farm_name': apply.farm_name,
            'applier_phone_number': apply.applier_phone_number,
            'period': apply.period,
            'details': apply.details,
            'use_farm': [{
                'farm_number': apply.use_farm_num,
                'farm_fish': apply.use_farm_fish,
                'farm_fish_amount': apply.use_amount
            }]
        } for apply in apply], 200)
