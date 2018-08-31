from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from app.models.farm import FarmModel
from app.views import BaseResource
from app.docs.user.farm.farm import SEARCH_FARM

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user'

doList = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
          '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']


@api.resource('/search')
class SearchFarm(BaseResource):
    @swag_from(SEARCH_FARM)
    @jwt_required
    def get(self):
        """
        양식장 검색
        """
        donum = int(request.args.get('donum'))
        do = doList[donum]

        all_farm = FarmModel.objects().all()

        if all_farm is None:
            return '', 204

        return self.unicode_safe_json_dumps([{
            'farmName': farm.farm_name,
            'farmMoney': farm.mini_farms[0].farm_cost,
        } for farm in all_farm if do in farm.farm_address], 200)


@api.resource('/search/<farmname>')
class SearchFarmInfo(BaseResource):
    @swag_from()
    @jwt_required
    def get(self, farmname):
        """

        """
        farm = FarmModel.objects(farm_name=farmname).first()

        if farm is None:
            abort(406)

        return self.unicode_safe_json_dumps([{
            'farm_name': farm.farm_name,
            'farm_phone_number': farm.farm_phone_number,
            'farm_address': farm.farm_address,
            'farm_details': farm.farm_details,
            'can_use_farm': [{
                'farm_number': minifarm.farm_number,
                'farm_cost': minifarm.farm_cost,
                'farm_fish_max': minifarm.farm_fish_max,
                'temperature': minifarm.temperature
            } for minifarm in farm.mini_farms]
        }], 200)

