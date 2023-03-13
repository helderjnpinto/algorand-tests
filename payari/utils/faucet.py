# Get funding for accounts
from utils.config import algod_client
from utils.client import get_dispenser_account_from_kmd
from utils.transactions import transfer


def check_dispenser_balance(addr):
    account_info = algod_client.account_info(addr)
    balance = account_info.get("amount")
    print('\033[91m'+'balance: ' + '\033[92m', balance)
    return balance > 10_000_000


def dispense(to_address, amount):
    pk, addr = get_dispenser_account_from_kmd()
    if check_dispenser_balance(addr):
        return transfer(pk, addr, to_address, amount)
    else:
        print("Dispenser account not have founds")
        exit(0)
