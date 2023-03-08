import subprocess
from contracts import get_tealish_list

complete_file_list, file_list = get_tealish_list()

for index, contractPath in enumerate(complete_file_list):
    compile_result = subprocess.run(["tealish", "compile", contractPath])
    print("The result for contract %s exit code was: %d" %
          (file_list[index], compile_result.returncode))
