from flask import Response, abort
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity

import json

# from app.models.admin.account import AdminModel


# @jwt_required 를 사용해서 토큰이 있는지 검증하고
# get_jwt_identity()를 사용해서 id를 가져와서 쿼리문 날려서 데이터베이스에서 정보 가져옴
# 그 정보에서 admin인지 아닌지 체크해서 admin이 아니라면 접근 불가능하게 해주는 admin_required 만들 거임


class BaseResource(Resource):

    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        """
        json 형식에서 utf-8 형식 한글이 깨지는 현상 방지.
        한글을 json 으로 보낼 때 unicode_safe_json_dumps를 사용한다.

        :param data: json type (dict)
        :param status_code: http status code
        """

        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )

    @classmethod
    def admin_required(cls):
        admin_id = get_jwt_identity()

        if AdminModel.objects(id=admin_id).first() is None:
            abort(403)

        return admin_id


class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from .admin.account import auth, signup
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(signup.api.blueprint)
        from .admin.farm import farm
        app.register_blueprint(farm.api.blueprint)
        from .admin.apply import apply_from_user, apply_store
        app.register_blueprint(apply_from_user.api.blueprint)
        app.register_blueprint(apply_store.api.blueprint)
        from .user.account import auth, signup
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(signup.api.blueprint)
        from .user.apply import apply_farm, apply_store
        app.register_blueprint(apply_farm.api.blueprint)
        app.register_blueprint(apply_store.api.blueprint)
        # from .user.farm import farm
        # app.register_blueprint(farm.api.blueprint)
        from .user.search import search
        app.register_blueprint(search.api.blueprint)
