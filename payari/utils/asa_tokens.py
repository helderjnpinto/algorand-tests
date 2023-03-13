from utils.config import algod_client
from utils.accounts import DEPLOYER_ADDRESS, DEPLOYER_PK
from algosdk import transaction


def create_asa_token(token_manager_private_key=None, token_manager_address="", unit_name="TOKEN", asset_name="My Custom Token", total=21_000_000_0000_0000, decimals=8):
    # Create the token creation transaction
    params = algod_client.suggested_params()
    txn = transaction.AssetConfigTxn(
        sender=token_manager_address,
        sp=params,
        total=total,  # total supply of the token
        default_frozen=False,  # allow accounts to opt-out of holding the token
        unit_name=unit_name,  # token ticker symbol
        asset_name=asset_name,  # token name
        manager=token_manager_address,  # the token manager's address
        reserve=token_manager_address,  # the address where unallocated tokens are held
        # the address that can freeze or unfreeze accounts from holding the token
        freeze=token_manager_address,
        # the address that can clawback the token from accounts
        clawback=token_manager_address,
        url="https://mycustomtoken.com",  # a URL containing information about the token
        decimals=decimals,  # the number of decimal places to use for fractional amounts of the token
    )

    signed_txn = txn.sign(token_manager_private_key)

    txId = algod_client.send_transaction(signed_txn)

    transaction_response = None
    while transaction_response is None:
        transaction_response = algod_client.pending_transaction_info(txId)

    asset_id = transaction_response.get("asset-index")

    return (asset_id, transaction_response)


def transferASA(token_id, sender_pk=DEPLOYER_PK, sender=DEPLOYER_ADDRESS, receiver_address="", amount=1_000_000):
    verify_token_opt_in(token_id, receiver_address)

    params = algod_client.suggested_params()
    txn = transaction.AssetTransferTxn(
        sender=sender,
        sp=params,
        receiver=receiver_address,
        amt=amount,
        index=token_id
    )
    signed_txn = txn.sign(sender_pk)
    txid = algod_client.send_transaction(signed_txn)
    print('\033[91m'+'transferASA txid: ' + '\033[92m', txid)
    transaction.wait_for_confirmation(algod_client, txid)
    # wait for it
    transaction_response = None
    while transaction_response is None:
        transaction_response = algod_client.pending_transaction_info(txid)

    print('\033[91m'+'transferASA transaction_response: ' +
          '\033[92m', transaction_response)
    return transaction_response


def verify_token_opt_in(token_id, receiver_address):
    # Verify that the receiver has opted-in to the token
    opted_in = algod_client.account_info(receiver_address)['assets'].get(
        str(token_id), {}).get('opted-in', False)
    print('\033[91m'+'opted_in: ' + '\033[92m', opted_in)
    if not opted_in:
        raise Exception('Receiver has not opted-in to the token')
    return opted_in
