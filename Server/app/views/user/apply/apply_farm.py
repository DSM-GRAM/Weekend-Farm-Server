from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.models.user.account.account import UserModel
from app.models.admin.farm.farm import FarmModel, MiniFarmModel
from app.models.user.apply.farm import FarmApplyModel, MiniFarmApplyModel
from app.views import BaseResource
from app.docs.user.farm.farm import SEARCH_FARM

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user/farm'


@api.resource('/apply/<farm_name>')
class SearchFarm(BaseResource):
    @swag_from()
    @jwt_required
    def post(self, farm_name):
        # """
        # 유저 양식장 신청
        # """
        # phone_num = request.json['phone_number'],
        # farm_period = request.json['farm_period']
        # # farm_period = '2018_01_01~2018_08_12'
        # details = request.json['details']
        # 
        # apply_farm = request.json['apply_farm']
        # 
        # # farm_period_first_point = farm_period[:9]
        # # farm_period_end_point = farm_period[11:]
        # 
        # farm = FarmModel.objects(farm_name=farm_name).first()
        # user = UserModel.objects(id=get_jwt_identity()).first()
        # 
        # minifarm_apply = MiniFarmApplyModel(
        #     mini_farm_number=apply_farm,
        #     mini_farm_fish_kind=farm.having_minifarm.minifarm_fish_kind,
        #     mini_farm_fish_number=farm.having_minifarm.minifarm_fish_number
        # )
        # 
        # apply = FarmApplyModel(
        #     user_name=user.name,
        #     user_phone_number=user.phone_number,
        #     period=farm_period,
        #     details=details,
        # )
        # 
        # apply.mini_farm_list.append(minifarm_apply)
        # apply.save()
        # 
        # return '', 201

# 모름 내일 할거임 기획을 제대로 이해 못한 탓
