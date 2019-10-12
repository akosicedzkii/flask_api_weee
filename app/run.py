from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restplus import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}
app = Flask(__name__)
api = Api(app = app,authorizations=authorizations,description='DevOps APIs',title = "DevOps APIs" )

SWAGGER_URL='/swagger'
API_URL ='/swagger.json'
name_space = api.namespace('auth', description='Auth APIs')

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app-name" : "Test"
    }
)

app.register_blueprint(swaggerui_blueprint,url_prefix=SWAGGER_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpassword@172.19.0.2/flask_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

import views, models, resources


api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin)
api.add_resource(resources.UserLogoutAccess)
api.add_resource(resources.UserLogoutRefresh)
api.add_resource(resources.TokenRefresh)
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')
api.add_resource(resources.SendEmail,'/send_email')


