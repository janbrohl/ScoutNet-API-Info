import json
import requests


SN_REST_BASE_URL = "https://www.scoutnet.de/api/0.2/"


def sn_rest(path, *args):
    if args:
        params = {
            "json": json.dumps(args)
        }
    else:
        params = {}
    return requests.get(
        SN_REST_BASE_URL + path,
        params=params
    ).json()
