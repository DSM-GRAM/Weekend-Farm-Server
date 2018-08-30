from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.models.admin.farm.farm import FarmModel
from app.models.admin.farm.used_farm import UsedFarmModel
from app.views import BaseResource
from app.docs.admin.farm.farm import ADMIN_ADD_INFORM, RETURN_ADMIN_ADD_INFORM


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin/farm'


@api.resource('/<num>')
class FarmInformation(BaseResource):
    @swag_from(RETURN_ADMIN_ADD_INFORM)
    @jwt_required
    def get(self):
        """
        관리자 양식장 정보 조회
        """
        farm = FarmModel.objects(farm_hostname=get_jwt_identity()).first())
        return ''
        # 개 힘듬 하

    @swag_from()
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

        room = payload['room']

        usedfarm = {
            'farm_number': room.farm_number,
            'farm_cost': room.farm_cost,
            'farm_fish_max': room.farm_fish_max
        }
        try:
            FarmModel(
                farm_name=farm_name,
                farm_hostname=get_jwt_identity(),
                farm_phone_number=farm_phone_num,
                farm_address=farm_address,
                farm_details=details,
                minifarm=usedfarm
            ).save()
        except TypeError:
            abort(406)

        return '', 201


