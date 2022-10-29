from flask_restful import Api
from api.characters.characters import Characters
from api.comics.comics import Comics

api = Api()

api.add_resource(Characters, "/name")
api.add_resource(Comics, "/comics")
