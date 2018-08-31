from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from app.models.apply import ApplyModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user/store'


@api.resource('')
class SearchFarm(BaseResource):
    @swag_from()
    @jwt_required
    def post(self, farm_name):
        """
        유저 양식장 상점 신청
        """

