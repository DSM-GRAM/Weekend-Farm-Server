from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.models.admin import AdminModel
from app.models.farm import FarmModel, MiniFarmModel, MiniFarmFishModel
from app.models.apply import ApplyModel
from app.views import BaseResource
from app.docs.admin.farm.farm import ADMIN_ADD_INFORM, RETURN_ADMIN_ADD_INFORM

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin/farm'


@api.resource('')
class FarmInformation(BaseResource):
    @swag_from(RETURN_ADMIN_ADD_INFORM)
    @jwt_required
    def get(self):
        """
        관리자 양식장 정보 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        farm = FarmModel.objects(farm_hostname=admin.name).first()

        return self.unicode_safe_json_dumps([{
            'room_cost': data.farm_cost,
            'room_fish_max': data.farm_fish_max,
            'room_number': data.farm_number,
            'room_temperature': data.temperature
        } for data in farm.mini_farms], 200) if admin or farm else abort(406)

    @swag_from(ADMIN_ADD_INFORM)
    @jwt_required
    def post(self):
        """
        관리자 양식장 정보 작성
        """
        payload = request.json

        farm_name = payload['farm_name']
        farm_phone_num = payload['farm_phone_num']
        farm_address = payload['farm_address']
        details = payload['details']

        rooms = payload['rooms']

        admin = AdminModel.objects(id=get_jwt_identity()).first()

        try:
            FarmModel(
                farm_name=farm_name,
                farm_hostname=FarmModel.farm_hostname.name,
                farm_phone_number=farm_phone_num,
                farm_address=farm_address,
                farm_details=details,
                mini_farms=rooms
            ).save()

        except TypeError:
            abort(406)

        return '', 201


@api.resource('/edit/<num>')
class EditExtensionOption(BaseResource):
    @swag_from()
    @jwt_required
    def post(self, num):
        """
        관리자 내 양식장 상황 작성
        """
        payload = request.json

        admin = AdminModel.objects(id=get_jwt_identity()).first()
        farm = FarmModel.objects(farm_hostname=admin.name).first()

        mini_farm = farm.mini_farms[num-1]

        MiniFarmFishModel(

        )


@api.resource('/list')
class ViewAdminMiniFarmList(BaseResource):
    @swag_from()
    @jwt_required
    def get(self):
        """
        관리자 신청 상황
        """
        farm = FarmModel.objects(farm_hostname=get_jwt_identity()).first()
        apply = ApplyModel.objects(farm_name=farm.farm_name).first()

        if farm is None or apply is None:
            abort(406)

        return self.unicode_safe_json_dumps([{
            'farm_number': farm.farm_number,
            'user_name': farm.user_name
        } for farm in farm.mini_farms], 200)
