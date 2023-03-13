from utils.config import algod_client
from utils.accounts import deployer_address, deployer_private_key
from algosdk import transaction


def transfer(sender_pk=deployer_private_key, sender=deployer_address, receiver_address="", amount=1_000_000):
    params = algod_client.suggested_params()
    txn = transaction.PaymentTxn(sender, params, receiver_address, amount)
    signed_txn = txn.sign(sender_pk)
    txid = algod_client.send_transaction(signed_txn)
    print('\033[91m'+'txid: ' + '\033[92m', txid)
    transaction.wait_for_confirmation(algod_client, txid)
    # wait for it
    transaction_response = None
    while transaction_response is None:
        transaction_response = algod_client.pending_transaction_info(txid)

    print('\033[91m'+'transfer transaction_response: ' +
          '\033[92m', transaction_response)
    return transaction_response


def get_sp():
    suggested = algod_client.suggested_params()
    suggested.flat_fee = True
    suggested.fee = 1_000
    return suggested


def call_application_noop_tx(app_id=0, app_args=[], sender_pk=deployer_private_key, sender_address=deployer_address):
    txn = transaction.ApplicationNoOpTxn(
        sp=get_sp(),
        sender=sender_address,
        index=app_id,
        app_args=app_args)

    signed_txn = txn.sign(sender_pk)
    print('\033[91m'+'signed_txn: ' + '\033[92m', signed_txn)
    txHash = algod_client.send_transaction(signed_txn)
    print('\033[91m'+'Transaction hash: ' + '\033[92m', txHash)
    confirmed_txn = algod_client.pending_transaction_info(txHash)
    print('\033[91m'+'confirmed_txn: ' + '\033[92m', confirmed_txn)

    while not confirmed_txn.get("confirmed-round"):
        confirmed_txn = algod_client.pending_transaction_info(txHash)

    return confirmed_txn


def delete_application(app_id=0, sender_pk=deployer_private_key, sender_address=deployer_address):
    txn = transaction.ApplicationDeleteTxn(
        sp=get_sp(),
        sender=sender_address,
        index=app_id,
    )

    signed_txn = txn.sign(sender_pk)
    txHash = algod_client.send_transaction(signed_txn)
    print('\033[91m'+'txHash: ' + '\033[92m', txHash)

    confirmed_txn = algod_client.pending_transaction_info(txHash)
    print('\033[91m'+'delete confirmed_txn: ' + '\033[92m', confirmed_txn)

    while not confirmed_txn.get("confirmed-round"):
        confirmed_txn = algod_client.pending_transaction_info(txHash)

    return confirmed_txn


def get_app_id_from_deploy_tx(txId):
    transaction_response = None
    while transaction_response is None:
        transaction_response = algod_client.pending_transaction_info(txId)

    app_id = transaction_response.get("application-index")

    return (app_id, transaction_response)
