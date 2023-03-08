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



# TODO: delete app fn
# Delete the app
# txn = transaction.ApplicationDeleteTxn(
#     sender=account1,
#     sp=params,
#     index=app_id,
# )
#
# signed_txn = txn.sign(account1_sk)
# txid = algod_client.send_transaction(signed_txn)
# print("Transaction ID: {}".format(txid))
#
# # Wait for wait_for_confirmation
# wait_for_confirmation(algod_client, txid)
#
#

# TODO: call application
# for i in range(1, 12):
#     params = algod_client.suggested_params()
#     params.flat_fee = True
#     params.fee = 1_000

# # ApplicationCallTxn(sender, sp, index, on_complete, local_schema=None, global_schema=None,
# # approval_program=None, clear_program=None, app_args=None,
# # accounts=None, foreign_apps=None, foreign_assets=None,
# # note=None, lease=None, rekey_to=None, extra_pages=0, boxes=None)
#     txn = transaction.ApplicationCallTxn(
#         sender=sender,
#         sp=params,
#         index=app_id,
#         on_complete=transaction.OnComplete.NoOpOC,
#     )
#     signed_txn = txn.sign(sender_pk)
#     txid = algod_client.send_transaction(signed_txn)
#     print("Transaction ID: {}".format(txid))
#     transaction.wait_for_confirmation(algod_client, txid)
