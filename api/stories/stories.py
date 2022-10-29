from flask_restful import Resource
from api.helpers import get_feature_thumbnails
from api.helpers import interpolate_marvel_api, get_results


class Stories(Resource):
    def get(self):
        feature = "stories"
        url = interpolate_marvel_api(feature)
        results = get_results(url)
        feature_filter = "title"
        stories_names_thumbnails = get_feature_thumbnails(results, feature_filter)

        return stories_names_thumbnails
