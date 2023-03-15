from utils.deploy import deploy
from utils.contracts import get_abi
from utils.applications import get_app_info, get_app_global_state
from utils.config import algod_client, SENDER_ADDRESS
from utils.transactions import call_application_noop_tx, delete_application
import pytest
import sys
import base64
from algosdk import abi
from algosdk.abi.base_type import ABIType
sys.path.append("..")


# Define a fixture to deploy a contract
@pytest.fixture(scope="module")
def deploy_contacts():
    app_id = 164520213
    # app_id, transaction_response, txId = deploy("payari")
    # print('\033[91m'+'app_id: ' + '\033[92m', app_id)
    # print('\033[91m'+'transaction_response: ' +
    #       '\033[92m', transaction_response)
    # print('\033[91m'+'transaction hash: ' + '\033[92m', txId)

    # Teardown the deployed contract using clear function
    yield (app_id, algod_client)

    # # Teardown the contract by deleting it from the Algod client
    # print('\033[91m'+'Teardown')
    # account_info = algod_client.account_info(SENDER_ADDRESS)
    # print("SENDER_ADDRESS Account {} balance: {} microAlgos".format(
    #     SENDER_ADDRESS, account_info.get('amount')) + "\n")
    # result = delete_application(app_id)
    # print('\033[91m'+'delete app result: ' + '\033[92m', result)


def print_logs(log):
    if b'%i' in log:
        i = log.index(b'%i')
        s = log[0:i].decode()
        value = int.from_bytes(log[i + 2:], 'big')
        return (s,value)
    else:
        return (None, None)


def test_contract_methods_log(deploy_contacts):
    app_id, algod_client = deploy_contacts

    # Test the contract's `add` method
    receipt = call_application_noop_tx(app_id, [b"add", 10, 20])

    print('\033[91m'+'receipt: ' + '\033[92m', receipt)

    logs = receipt['logs'][0]
    string_value, parsed_integer = print_logs(base64.b64decode(logs))
    print('\033[91m'+'string_value: ' + '\033[92m', string_value, parsed_integer)

    # msg1 = base64.b64decode("FR98dQAAAAAAAASD")[4:]
    # print('\033[91m'+'msg1: ' + '\033[92m', msg1)
    # dec = codec.decode(msg1)
    # print('\033[91m'+'dec: ' + '\033[92m', dec)

    # log = receipt['logs'][0]
    # print('\033[91m'+'>>>>>>>>>>>>>>>>> log: ' + '\033[92m', log)
    
    # codec = ABIType.from_string("string")
    # logBase64 = base64.b64decode(log)[4:]
    # print('\033[91m'+'logBase64: ' + '\033[92m', logBase64)
    # out = codec.decode(logBase64)
    # print('\033[91m'+'>>>>>>>>>>>>>>>>> out: ' + '\033[92m', out)
    compiled_log = string_value + "%i " + str(parsed_integer)

    assert compiled_log == "add return value logx %i 30"

    assert receipt['logs'][0] == 'YWRkIHJldHVybiB2YWx1ZSBsb2d4ICVpAAAAAAAAAB4='
    # global_state = algod_client.application_state(contract_address).get("result").get("global-state")
    # assert global_state[0].get("value").get("uint") == 30
    assert True
