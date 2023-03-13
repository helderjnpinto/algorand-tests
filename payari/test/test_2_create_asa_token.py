from utils.config import algod_client
from utils.accounts import deployer_address, create_account
from utils.asa_tokens import create_asa_token, transfer_asa, opt_in_token
from utils.faucet import dispense
import pytest
import sys
sys.path.append("..")


def pytest_namespace():
    return { 'asset_index': None }


def test_create_asa_token():
    asa_id, _ = create_asa_token()
    print('\033[91m'+'asa_id: ' + '\033[92m', asa_id)
    
    assert asa_id > 0
    pytest.asset_index = asa_id


def test_transfer_asa_token():
    asset_index = pytest.asset_index

    receiver_pk, receiver = create_account()
    dispense(receiver, 1_000_000)

    balance_before = algod_client.account_info(receiver)
    print('\033[91m'+'balance_before: ' + '\033[92m', balance_before)
    assert balance_before.get("amount") == 1_000_000

    balance_before_asa = algod_client.account_asset_info(deployer_address, asset_index)
    print('\033[91m'+'balance_before_asa: ' + '\033[92m', balance_before_asa)

    opt_in_token(asset_index, receiver_pk, receiver)

    balance_before = algod_client.account_info(receiver)
    print('\033[91m'+'>>>>balance_before: ' + '\033[92m', balance_before)


    tx = transfer_asa(asset_index, receiver, 10)
    print('\033[91m'+'tx: ' + '\033[92m', tx)

    # balance_after_asa = algod_client.account_asset_info(receiver, asset_index)
    # print('\033[91m'+'balance_after_asa: ' + '\033[92m', balance_after_asa)
    # assert balance_after_asa == 10
