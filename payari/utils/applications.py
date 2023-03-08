from utils.config import algod_client


def get_app_info(app_id):
    app_info = algod_client.application_info(app_id)
    print('\033[91m'+'app_info: ' + '\033[92m {}'.format(app_info))
    return app_info


def get_app_global_state(app_id):
    app_global_state = algod_client.application_boxes(app_id)
    print('\033[91m'+'get_app_global_state: ' +
          '\033[92m {}'.format(app_global_state))
    return app_global_state
