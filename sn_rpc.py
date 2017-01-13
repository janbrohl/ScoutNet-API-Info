import os
import requests


SN_RPC_URL = "https://www.scoutnet.de/jsonrpc/server.php"


class RPCError(Exception):
    pass


def rpc(url, method, *params):
    """
    JSON-RPC 1.0 über HTTP(S) POST
    """
    call_id = os.urandom(16).hex()
    json_data = {
        "method": method,
        "params": params,
        "id": call_id
    }
    got = requests.post(
        url,
        json=json_data
    ).json()
    e = got["error"]
    if e is not None:
        raise RPCError(e)
    return got["result"]


def sn_rpc_get(*params):
    return rpc(
        SN_RPC_URL,
        "get_data_by_global_id",
        *params
    )
