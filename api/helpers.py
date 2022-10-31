"""Helper functions for all apis"""
import time
import hashlib
import requests

from api.config import (
    BASE_URL_MARVEL,
    SECRET_KEY,
    PUBLIC_KEY,
)


def interpolate_marvel_api(feature):
    """This functions performs the neccessary steps to use marvel's api"""
    url = BASE_URL_MARVEL + feature + "?"
    timestamp = time.time()
    string_to_hash = str(timestamp) + SECRET_KEY + PUBLIC_KEY
    hashmd5 = hashlib.md5(string_to_hash.encode("utf-8")).hexdigest()
    auth = f"ts={timestamp}&apikey={PUBLIC_KEY}&hash={hashmd5}&limit=20"
    return url + auth


def get_feature_thumbnails(results, attribute):
    "Helper function that returns a list of features' stories and thumbnails"
    feature_thumbnails = []
    for result in results:
        feature = result.get(attribute, f"{attribute} Not Available")
        thumbnail = result.get("thumbnail", None)
        if thumbnail is None:
            thumbnail = interpolate_missing_thumbnail_dict()
        current_char = {attribute: feature, "thumbnail": thumbnail}
        feature_thumbnails.append(current_char)

    return feature_thumbnails


def interpolate_missing_thumbnail_dict():
    """This functions creatues thumbnail dict incase it's missing from api"""
    return {
        "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
        "extension": "jpg",
    }


def get_results(url):
    """Helper function to get results from api provided a url"""
    resp = requests.get(url=url)
    response_dict = resp.json()

    # Todo : response.raise_for_status() implement with an exception
    return response_dict["data"]["results"]
