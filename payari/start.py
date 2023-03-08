from utils.deploy import *
from utils.applications import *

app_id, _ = deploy("payari")

info = get_app_info(app_id)
app_global_state = get_app_global_state(app_id)

