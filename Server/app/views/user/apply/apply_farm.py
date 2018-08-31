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
        """
        유저 양식장 신청
        """
        pass