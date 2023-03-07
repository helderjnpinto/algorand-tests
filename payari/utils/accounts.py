from algosdk import v2client, account, mnemonic
from config import algod_client, SENDER_ADDRESS, SENDER_MNEMONIC

# Get account address from mnemonic
sk = mnemonic.to_private_key(SENDER_MNEMONIC)
addr = account.address_from_private_key(sk)

if addr != SENDER_ADDRESS:
    print("ENV FOR sender address is not equal to imported mnemonic")
    exit(1)

# Get current blockchain balance of account
account_info = algod_client.account_info(addr)
balance = account_info.get("amount")

# Print address and balance
print("Address:", addr)
print("Balance:", balance)
