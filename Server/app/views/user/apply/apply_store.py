from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.apply import ItemApplyModel
from app.models.store import StoreModel
from app.models.user import UserModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user/store'


@api.resource('/apply')
class SearchFarm(BaseResource):
    @jwt_required
    def get(self):
        """
        유저 상점 아이템 보여주는 API
        """
        items = StoreModel.objects(user=UserModel.objects(id=get_jwt_identity()).first()).all()

        return self.unicode_safe_json_dumps([{
            'cItemName': item.itemName,
            'cItemNum': item.itemNum,
            'money': item.money
        } for item in items], 200)

    @jwt_required
    def post(self):
        """
        유저 상점 아이템 구입 요청 API
        """
        itemNum = request.json['bItemNum']
        itemName = request.json['bItemName']
        money = request.json['pMoney']

        ItemApplyModel(
            itemNum=itemNum,
            itemName=itemName,
            money=money
        ).save()

        return '', 201


@api.resource('/apply/secret')
class Secret(BaseResource):
    @jwt_required
    def post(self):
        itemName = request.json['itemName']
        itemNum = request.json['itemNum']
        money = request.json['money']
        details = request.json['details']

        StoreModel(
            user=UserModel.objects(id=get_jwt_identity()).first(),
            itemName=itemName,
            itemNum=itemNum,
            money=money,
            details=details
        ).save()

        return '', 201


