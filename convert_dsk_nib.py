
import os
from os import listdir, path
from os.path import isfile, join
import subprocess


def convert(path, name):

    process = subprocess.Popen([working_path + '/dsk2nib.exe', name + '.dsk', name + '.nib'], 
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break
        

#indicar o caminho para o diretorio onde estao os arquivos
working_path = "C:/Users/augba/Desktop/Emuladores/_roms/apple2/dsk"

onlyfiles = [f for f in listdir(working_path) if isfile(join(working_path, f)) and f.lower().endswith(".dsk")]

for f in onlyfiles:
    filename = f.lower()
    filename = filename[:-4]
    print("------------")
    print(filename)
    convert(working_path, filename)
    
