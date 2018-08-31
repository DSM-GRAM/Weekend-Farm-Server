from flask import Blueprint, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.models.user import UserModel
from app.models.apply import ApplyModel, RoomModel
from app.views import BaseResource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/user/farm'


@api.resource('/apply')
class SearchFarm(BaseResource):
    @swag_from()
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

        ApplyModel(
            user=user,
            applyDate=period,
            message=details,
            roominfo=[RoomModel(
                rNum=roominfo.rNum,
                rFishKind=roominfo.rFishKind,
                rAmount=roominfo.rAmount
            ) for roominfo in roominfos]
        ).save()

        return '', 201
