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

        minifarms = [MiniFarmModel(**data, admin=admin).save() for data in rooms]

        try:
            FarmModel(
                farm_name=farm_name,
                farm_hostname=FarmModel.farm_hostname.name,
                farm_phone_number=farm_phone_num,
                farm_address=farm_address,
                farm_details=details,
                mini_farms=minifarms
            ).save()
        except TypeError:
            abort(406)

        return '', 201


@api.resource('/edit/<num>')
class EditExtensionOption(BaseResource):
    @swag_from()
    @jwt_required
    def get(self, num):
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        farm = FarmModel.objects(farm_hostname=admin.name).first()
        apply = ApplyModel.objects(farm=FarmModel.objects(farm_name=farm.farm_name).first()).first()
        minifarm = farm.mini_farms[num-1]

        return self.unicode_safe_json_dumps({
            'name': apply.user.name,
            'phone_number': apply.user.phone_number,
            'period': apply.period,
            'temperature': minifarm.temperature,
            'farm_cost': minifarm.farm_cost,
            'fish_kind': [{
                'kind': data.kind,
                'amount': data.amount
            } for data in minifarm.fish_kind],
            'details': minifarm.details
        })

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

        mini_farm.update(
            temperature=payload['temperature'],
            farm_cost=payload['cost'],
            fish_kind=payload['fish_kind'],
            # payload['fish_kind'] = [{
            #   'kind': 'String'
            #   'amount': 'Int'
            # }
            details=payload['details']
        ).save()

        return '', 201


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
