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
        itemName = request.json['itemName']
        itemNum = request.json['itemNum']
        # 개당 가격
        money = request.json['money']
        details = request.json['details']

        StoreModel(
            itemName=itemName,
            itemNum=itemNum,
            money=money,
            details=details
        ).save()

        return '', 201
