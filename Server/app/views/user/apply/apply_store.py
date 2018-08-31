from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.models.store import StoreModel
from app.models.user import UserModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user/farm'


@api.resource('/apply/<farm_name>')
class SearchFarm(BaseResource):
    @swag_from()
    @jwt_required
    def post(self):
        """
        유저 상점 아이템 신청
        """
        user = UserModel.objects(id=get_jwt_identity()).first()
        product = request.json['product']

        StoreModel(
           user=name,


        ).save()

        return '', 200