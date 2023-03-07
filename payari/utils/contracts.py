import os

# get the directory of the current script
script_dir = os.path.dirname(__file__)
contracts_path = '../contracts/tealish/'
contracts_path = os.path.join(script_dir, contracts_path);
file_list = os.listdir(contracts_path)
complete_file_list = []

for file_name in file_list:
    complete_file_list.append(contracts_path + file_name)
