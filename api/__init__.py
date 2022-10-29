from flask_restful import Api
from api.characters.characters import Characters

api = Api()

api.add_resource(Characters, "/name")
