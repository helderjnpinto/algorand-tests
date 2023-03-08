import subprocess


def compile_contracts(file_list, complete_file_list):
    compile_results = []
    
    for index, contractPath in enumerate(complete_file_list):
        print('\n\t (info) compile: %s ' % file_list[index])

        compile_result = subprocess.run(["tealish", "compile", contractPath])
        compile_results = compile_results.append(compile_results)
        print("\t (debug) The result for contract %s exit code was: %d" %
              (file_list[index], compile_result.returncode))

    return compile_results
