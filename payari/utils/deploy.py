from utils.contracts import load_contract
from utils.config import algod_client
from utils.accounts import DEPLOYER_ADDRESS, DEPLOYER_PK
from utils.transactions import get_app_id_from_deploy_tx
from algosdk import encoding
from algosdk.transaction import ApplicationCreateTxn
from algosdk import transaction
from pyteal import *


def clear_program():
    return Return(Int(1))


def clear_program_bytes():
    teal_program = compileTeal(clear_program(), Mode.Application, version=7)
    teal_program_base64 = algod_client.compile(teal_program)["result"]
    return_data_bytes = encoding.base64.b64decode(teal_program_base64)

    return return_data_bytes


def contract_contents_to_base64(source_code):
    compiled_bytes = algod_client.compile(source_code, True)
    # print('\033[91m'+'compiled_bytes: ' + '\033[92m', compiled_bytes)
    base64_program = encoding.base64.b64decode(compiled_bytes["result"])
    return (base64_program, compiled_bytes)


# TODO: PASS GLOBAL SCHEMA AND LOCAL SCHEMA
def deploy(contract_name, sender_address=DEPLOYER_ADDRESS, sender_private_key=DEPLOYER_PK):
    source_code = load_contract(contract_name)
    base64_program, _ = contract_contents_to_base64(source_code)

    # Deploy our contract
    suggested = algod_client.suggested_params()
    suggested.flat_fee = True
    suggested.fee = 1_000

    # create tx payload
    # https://py-algorand-sdk.readthedocs.io/en/latest/algosdk/transaction.html?highlight=ApplicationCreateTxn#algosdk.transaction.ApplicationCreateTxn
    txn = ApplicationCreateTxn(
        sp=suggested,
        sender=sender_address,
        approval_program=base64_program,
        clear_program=clear_program_bytes(),
        global_schema=transaction.StateSchema(1, 0),
        local_schema=transaction.StateSchema(0, 0),
        on_complete=transaction.OnComplete.NoOpOC,
        app_args=[]
    )

    #  sign tx
    signed_txn = txn.sign(sender_private_key)

    #  send tx
    txId = algod_client.send_transaction(signed_txn)
    print('\033[91m contract: ' + contract_name +
          ' with txId: ' + '\033[92m', contract_name, txId)

    app_id, transaction_response = get_app_id_from_deploy_tx(txId)

    print('\033[91m contract: ' + contract_name +
          'app_id: ' + '\033[92m', app_id)

    return (app_id, transaction_response, txId)
