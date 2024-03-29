from dotenv import load_dotenv
import os
from algosdk import v2client

load_dotenv()

# Set up Algod client
ALGOD_TOKEN = os.getenv('ALGOD_TOKEN')
print('\033[91m'+'ALGOD_TOKEN: ' + '\033[92m', ALGOD_TOKEN)
ALGOD_ADDR = os.getenv('ALGOD_ADDR')
print('\033[91m'+'ALGOD_ADDR: ' + '\033[92m', ALGOD_ADDR)

headers = {
   "X-API-Key": ALGOD_TOKEN,
}

algod_client = v2client.algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDR, headers)

try:
    algod_client.status()
except Exception as e:
    print("Algod Error: {}".format(e))

# Get account address from mnemonic
SENDER_ADDRESS = os.getenv('SENDER_ADDRESS')
SENDER_MNEMONIC = os.getenv('SENDER_MNEMONIC')
