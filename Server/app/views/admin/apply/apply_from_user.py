from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from app.views import BaseResource

blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin/apply'


@api.resource('')
class ApplyFromUser(BaseResource):
    @swag_from()
    @jwt_required
    def get(self):
        """
        유저가 보낸 신청을 불러오는 API
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()

        return '', 201
