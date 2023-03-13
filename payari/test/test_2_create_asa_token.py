from utils.deploy import deploy
from utils.contracts import get_abi
from utils.applications import get_app_info, get_app_global_state
from utils.config import algod_client
from utils.accounts import DEPLOYER_PK, DEPLOYER_ADDRESS
from utils.asa_tokens import create_asa_token
import sys
from algosdk import abi
from algosdk.abi.base_type import ABIType
sys.path.append("..")


asset_index

def test_create_asa_token():
    asset_index, _ = create_asa_token(DEPLOYER_PK, DEPLOYER_ADDRESS)
    print('\033[91m'+'asset_index: ' + '\033[92m', asset_index)
    
    assert