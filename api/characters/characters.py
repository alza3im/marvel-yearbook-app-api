from flask_restful import Resource
from api.helpers import get_feature_thumbnails
from api.helpers import interpolate_marvel_api, get_results


class Characters(Resource):
    def get(self):
        feature = "characters"
        attribute = "name"

        url = interpolate_marvel_api(feature)
        results = get_results(url)
        character_names_thumbnails = get_feature_thumbnails(results, attribute)

        return character_names_thumbnails
