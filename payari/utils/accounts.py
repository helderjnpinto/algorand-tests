from algosdk import v2client, account, mnemonic
from utils.config import algod_client, SENDER_ADDRESS, SENDER_MNEMONIC
import requests

# TODO: create fn generate accounts
# private_key, address = account.generate_account()


# Get account address from mnemonic
sender_mnemonic = mnemonic.to_private_key(SENDER_MNEMONIC)
sender_address = account.address_from_private_key(sender_mnemonic)

if sender_address != SENDER_ADDRESS:
    print("ENV FOR sender address is not equal to imported mnemonic")
    exit(1)

# Get current blockchain balance of account
account_info = algod_client.account_info(sender_address)
balance = account_info.get("amount")
print("Default sender address:", sender_address, " balance:", balance)

DEPLOYER_PK = sender_mnemonic
DEPLOYER_ADDRESS = sender_address

# UTILS
ZERO_ADDRESS = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
