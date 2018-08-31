from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from app.views import BaseResource

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin'


@api.resource('/farm/<num>')
class AdminEditSituation(BaseResource):
    @swag_from()
    @jwt_required
    def post(self, num):
        """
        관리자 내 양식장 상황 작성
        """
        payload = request.json

        temperature = payload['farm_temperature']
        fish = payload['farm_fish']
        details = payload['details']

        # admin = AdminModel.objects(id=get_jwt_identity()).first()
        # farm = FarmModel.objects(farm_hostname=admin.name).first()
        # apply_farm = FarmApplyModel.objects(farm_name=farm.farm_name)
        #
        # FarmManageModel(
        #     farm_number=num,
        #     farm_user=apply_farm.user_name,
        #     user_phone_number=apply_farm.user_phone_number,
        #     farm_period=apply_farm.period,
        #     farm_temperature=temperature,
        #     farm_fish=[{
        #         'kind': fish.kind,
        #         'amount': fish.amount
        #     } for fish in fish],
        #     farm_item='?',
        #     farm_details=details,
        #     all_money=int(farm.mini_farms[num-1].farm_cost)
        # ).save()
        #
        # return '', 201
