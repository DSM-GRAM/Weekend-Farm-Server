from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required

from app.models.user import UserModel
from app.models.apply import ApplyModel, RoomModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user/farm'


@api.resource('/apply')
class SearchFarm(BaseResource):
    @jwt_required
    def post(self):
        """
        유저 양식장 신청
        """
        user_phone_number = request.json['phoneNum']
        period = request.json['applyDate']
        details = request.json['message']
        roominfos = request.json['roominfo']

        user = UserModel.objects(phone_number=user_phone_number).first()

        roominfo = [RoomModel(**data) for data in roominfos]

        ApplyModel(
            user=user,
            applyDate=period,
            message=details,
            roominfo=roominfo
        ).save()

        return '', 201
