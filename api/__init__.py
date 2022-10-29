from flask_restful import Api
from api.characters.characters import Characters
from api.comics.comics import Comics
from api.stories.stories import Stories
from api.series.series import Series

api = Api()

api.add_resource(Characters, "/name")
api.add_resource(Comics, "/comics")
api.add_resource(Stories, "/stories")
api.add_resource(Series, "/series")
