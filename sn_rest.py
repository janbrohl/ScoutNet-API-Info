import json
import requests


def sn_rest(path, *args):
    if args:
        params = {"json": json.dumps(args)}
    else:
        params = {}
    return requests.get(SN_REST_BASE_URL + path, params=params).json()
