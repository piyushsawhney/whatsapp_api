from abc import abstractmethod, ABC
from flask import current_app as app
from flask_restful import Resource


class IUserServiceApi(Resource):
    @abstractmethod
    def get(self):
        pass
