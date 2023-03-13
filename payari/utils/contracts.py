import os
from utils.compile import compile_contracts
from pyteal import *


def get_contracts_list(relative_path):
    script_dir = os.path.dirname(__file__)
    contracts_path = os.path.join(script_dir, relative_path)
    files_and_dirs = os.listdir(contracts_path)
    file_list = [f for f in files_and_dirs if os.path.isfile(
        os.path.join(contracts_path, f))]

    file_list_path = []

    for file_name in file_list:
        file_list_path.append(contracts_path + file_name)

    return file_list, file_list_path


def get_tealish_list():
    return get_contracts_list('../contracts/')


def get_teal_list():
    return get_contracts_list('../contracts/build/')


def run_compile():
    file_list, complete_file_list = get_tealish_list()
    return compile_contracts(file_list, complete_file_list)


def load_teal_file_by_name(teal_file):
    script_dir = os.path.dirname(__file__)
    contract_path = os.path.join(script_dir, "../contracts/build/" + teal_file)
    file = open(contract_path, "r")
    return file.read()


def load_contract(contract_name, force_compile=True):
    tealish_list, _ = get_tealish_list()
    teal_list, _ = get_teal_list()

    # check changes in contracts folders
    if (force_compile or len(tealish_list) != len(teal_list)):
        run_compile()
        teal_list, _ = get_teal_list()

    filtered_list = list(
        filter(lambda x: x == contract_name + ".teal", teal_list))

    if len(filtered_list) == 1:
        return load_teal_file_by_name(filtered_list[0])
    else:
        raise ValueError("Contract name not found.")


def get_abi(contract_name):
    source_code = load_contract(contract_name)
    teal_code = """
    #pragma version 3
    int 0
    """
    return compileTeal(teal_code, Mode.Application)
