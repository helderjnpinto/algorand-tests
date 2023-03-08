from utils.config import algod_client
from utils.accounts import DEPLOYER_PK
from algosdk import transaction


def transfer(sender_pk=DEPLOYER_PK, amount=1_000_000, to_address=""):
    params = algod_client.suggested_params()
    txn = transaction.PaymentTxn(sender, params, to_address, amount)
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
