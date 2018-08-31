from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from app.views import BaseResource
from app.models.store import StoreModel


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin/apply'


@api.resource('/store')
class AdminApplyStore(BaseResource):
    @swag_from()
    @jwt_required
    def get(self):
        pass

    @swag_from()
    @jwt_required
    def post(self):
        """
        관리자 상점 추가
        """
        product = request.json['product']
        cost = request.json['cost']
        # 개당 가격
        details = request.json['details']

        StoreModel(
            store_product=product,
            store_cost=cost,
            store_details=details
        ).save()

        return '', 201
