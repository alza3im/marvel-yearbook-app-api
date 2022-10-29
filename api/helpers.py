"""Helper functions for all apis"""
import time
import hashlib

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
