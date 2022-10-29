from flask_restful import Resource
from api.helpers import get_feature_thumbnails
from api.helpers import interpolate_marvel_api, get_results


class Comics(Resource):
    def get(self):
        feature = "comics"
        attribute = "title"

        url = interpolate_marvel_api(feature)
        results = get_results(url)
        comics_names_thumbnails = get_feature_thumbnails(results, attribute)

        return comics_names_thumbnails
