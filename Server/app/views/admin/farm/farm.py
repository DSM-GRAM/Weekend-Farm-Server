from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.docs.admin.farm.farm import ADMIN_ADD_INFORM, RETURN_ADMIN_ADD_INFORM


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)
api.prefix = '/admin/farm'


@api.resource('')
class FarmInformation(BaseResource):
    @swag_from(RETURN_ADMIN_ADD_INFORM)
    def get(self):
        """
        관리자 양식장 정보 조회
        """
        pass

    @swag_from(ADMIN_ADD_INFORM)
    def post(self):
        """
        관리자 양식장 정보 작성
        """
        pass
