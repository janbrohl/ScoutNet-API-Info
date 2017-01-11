import json
import requests
import os

SN_REST_BASE_URL = "https://www.scoutnet.de/api/0.2/"

SN_RPC_URL = "https://www.scoutnet.de/jsonrpc/server.php"


def sn_rest(path, *args):
    if args:
        params = {"json": json.dumps(args)}
    else:
        params = {}
    return requests.get(SN_REST_BASE_URL + path, params=params).json()


class RPCError(Exception):
    pass


def rpc(url, method, *params):  # Client für JSON-RPC 1.0 über HTTP(S) POST
    call_id = os.urandom(16).hex()
    json_data = {"method": method, "params": params, "id": call_id}
    got = requests.post(url, json=json_data).json()
    e = got["error"]
    if e is not None:
        raise RPCError(e)
    return got["result"]


def sn_rpc_get(*params):
    return rpc(SN_RPC_URL, "get_data_by_global_id", *params)
