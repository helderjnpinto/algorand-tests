from dotenv import load_dotenv
import os
from algosdk import v2client

load_dotenv()


# Set up Algod client
ALGOD_TOKEN = os.getenv('ALGOD_TOKEN')
ALGOD_ADDR = os.getenv('ALGOD_ADDR')
algod_client = v2client.algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDR)

# Get account address from mnemonic
SENDER_ADDRESS = os.getenv('SENDER_ADDRESS')
SENDER_MNEMONIC = os.getenv('SENDER_MNEMONIC')