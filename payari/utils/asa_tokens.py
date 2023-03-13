from utils.config import algod_client
from utils.accounts import DEPLOYER_ADDRESS, DEPLOYER_PK
from algosdk import transaction


def create_asa_token(token_manager_private_key=DEPLOYER_PK, token_manager_address=DEPLOYER_ADDRESS, unit_name="TOKEN", asset_name="My Custom Token", total=21_000_000_0000_0000, decimals=8):
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
        # the number of decimal places to use for fractional amounts of the token
        decimals=decimals,
    )

    signed_txn = txn.sign(token_manager_private_key)

    txId = algod_client.send_transaction(signed_txn)

    transaction_response = None
    while transaction_response is None:
        transaction_response = algod_client.pending_transaction_info(txId)

    asset_id = transaction_response.get("asset-index")

    return (asset_id, transaction_response)


def transfer_asa(token_id, receiver_address="", amount=1_000_000, sender_pk=DEPLOYER_PK, sender_address=DEPLOYER_ADDRESS):
    print('\033[91m'+'token_id: ' + '\033[92m', token_id)
    verify_token_opt_in(token_id, receiver_address)

    params = algod_client.suggested_params()
    print('\033[91m'+'params123: ' + '\033[92m', params)
    txn = transaction.AssetTransferTxn(
        sender=sender_address,
        sp=params,
        receiver=receiver_address,
        amt=amount,
        index=token_id
    )
    signed_txn = txn.sign(sender_pk)
    print('\033[91m'+'signed_txn: ' + '\033[92m', signed_txn)
    tx_id = algod_client.send_transaction(signed_txn)
    print('\033[91m'+'transferASA tx_id: ' + '\033[92m', tx_id)
    transaction.wait_for_confirmation(algod_client, tx_id)
    # wait for it
    transaction_response = None
    while transaction_response is None:
        transaction_response = algod_client.pending_transaction_info(tx_id)

    print('\033[91m'+'transferASA transaction_response: ' +
          '\033[92m', transaction_response)
    return transaction_response


def is_opt_in(assets, token_id):
    if assets == []:
        return False
    
    return any(asset['asset-id'] == token_id for asset in assets)


def verify_token_opt_in(token_id, receiver_address):
    assets = algod_client.account_info(receiver_address)['assets']
    # Verify that the receiver has opted-in to the token
    opted_in =  is_opt_in(assets, token_id) 

    if not opted_in:
        raise Exception('Receiver has not opted-in to the token')
    return opted_in


def opt_in_token(token_id, sender_pk, sender_address):
    params = algod_client.suggested_params()
    txn = transaction.AssetOptInTxn(
        sender=sender_address,
        sp=params,
        index=token_id
    )

    signed_txn = txn.sign(sender_pk)

    txId = algod_client.send_transaction(signed_txn)

    transaction_response = None
    while transaction_response is None:
        transaction_response = algod_client.pending_transaction_info(txId)

    print('\033[91m'+'transaction_response: ' +
          '\033[92m', transaction_response)

    return transaction_response
