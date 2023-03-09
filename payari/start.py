from utils.deploy import deploy
from utils.contracts import get_abi
from utils.applications import get_app_info, get_app_global_state

# app_id, _ = deploy("payari")

# info = get_app_info(app_id)
# app_global_state = get_app_global_state(app_id)


abi = get_abi("payari")
print('\033[91m'+'abi: ' + '\033[92m', abi)
 