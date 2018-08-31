from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from app.models.apply import ApplyModel
from app.views import BaseResource


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
        user_phone_number = request.json['applier_phone_number']
        period = request.json['period ']
        details = request.json['details']
        # use_farm = request.json['farm']

        ApplyModel(
            user_phone_number=user_phone_number,
            period=period,
            details=details
        ).save()

        return '', 201
