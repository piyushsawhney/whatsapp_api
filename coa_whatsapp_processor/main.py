from flask import Flask
from flask_restful import Api

from coa_whatsapp_processor.application.api_implementation.user_service_impl import UserServiceApi

app = Flask(__name__)
api = Api(app)

api.add_resource(UserServiceApi, '/api/v1/user')

if __name__ == '__main__':
    app.run(debug=True)