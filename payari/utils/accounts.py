from algosdk import account, mnemonic
from utils.config import algod_client, SENDER_ADDRESS, SENDER_MNEMONIC

# Get account address from mnemonic
deployer_private_key = mnemonic.to_private_key(SENDER_MNEMONIC)
deployer_address = account.address_from_private_key(deployer_private_key)

if deployer_address != SENDER_ADDRESS:
    print("ENV FOR sender address is not equal to imported mnemonic")
    exit(1)

# Get current blockchain balance of account
account_info = algod_client.account_info(deployer_address)
balance = account_info.get("amount")
print("Default sender address:", deployer_address, " balance:", balance)

DEPLOYER_PK = deployer_private_key
DEPLOYER_ADDRESS = deployer_address

# Create accounts for testing

def create_account():
    private_key, address = account.generate_account()
    return (private_key, address)


def create_receiver_only_account():
    _, address = account.generate_account()
    print('\033[91m'+'address: ' + '\033[92m', address)
    return address

