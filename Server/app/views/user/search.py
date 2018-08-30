from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from app.models.admin.farm.farm import FarmModel
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
    def post(self):
        """
        양식장 검색
        """
        donum = request.json['donum']

        do = str(doList[donum - 1])

        all_farm = FarmModel.objects(farm_address_do=do).all()

        return [{
            'farm_name': farm.farm_name,
            'farm_phone_number': farm.farm_phone_number,
            'farm_address': farm.farm_address,
            'farm_details': farm.farm_details
        } for farm in all_farm], 200 if all_farm else Response('', 204)
