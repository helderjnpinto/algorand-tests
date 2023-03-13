import requests
from utils.config import ALGOD_ADDR, ALGOD_TOKEN
from algosdk import kmd


def algo_api_get_req(path, base=ALGOD_ADDR):
    url = base + path
    return requests.get(url, headers={"x-algo-api-token": ALGOD_TOKEN})


def algo_kmd_get_req(path, base="http://localhost:4002"):
    url = base + path
    # TODO: add proper env for algo token
    return requests.get(url, headers={"X-KMD-API-Token": ALGOD_TOKEN})


# https://github.com/algorand/js-algorand-sdk/blob/develop/src/client/kmd.ts
# wallets = wallet_list().json()
def wallet_list():
    return algo_kmd_get_req("/v1/wallets")


def get_dispenser_account_from_kmd():
    kmd_client = kmd.KMDClient(ALGOD_TOKEN, "http://localhost:4002")
    wallets = kmd_client.list_wallets()
    wallet_id = wallets[0]["id"]
    wallet_handle_token = kmd_client.init_wallet_handle(wallet_id, "")
    addresses = kmd_client.list_keys(wallet_handle_token)

    if (len(addresses) > 0):
        address = addresses[0]
        private_key = kmd_client.export_key(wallet_handle_token, "", address)
        return (private_key, address)
    else:
        print("Load kmd accounts not found any address")
        exit(1)
