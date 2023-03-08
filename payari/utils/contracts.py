import os
import subprocess

# compiled
compiled_contracts_path = '../contracts/tealish/build/'
compiled_contracts_path = os.path.join(script_dir, compiled_contracts_path)
compiled_files_and_dirs = os.listdir(contracts_path)
compiled_file_list = [f for f in files_and_dirs if os.path.isfile(
    os.path.join(contracts_path, f))]


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
    get_contracts_list('../contracts/tealish/')


def get_teal_list():
    get_contracts_list('../contracts/tealish/build/')


def compile_contracts():
    script_path = "utils/compile.py"
    subprocess.run(["python3", script_path])


def load_contract(contract_name):
    print(file_list)
    # compile_contracts()
    filtered_list = list(filter(lambda x: x == contract_name, file_list))

    if len(filtered_list) == 1:
        return filtered_list[0]
    else:
        raise ValueError("Contract name not found.")
