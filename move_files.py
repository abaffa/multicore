
import os
from os import listdir, path
from os.path import isfile, join

#indicar o caminho para o diretorio onde estao os arquivos
working_path = "E:/roms/mastersystem"

onlyfiles = [f for f in listdir(working_path) if isfile(join(working_path, f))]

page = 1
max_files = 125


current_file = 0


for f in onlyfiles:

    dir_name = "dir%02d" % page
    dir_path = working_path + "/" + dir_name

    source_path =  working_path + "/" + f
    destination_path = dir_path + "/" + f

    if not path.exists(dir_path):
        os.mkdir(dir_path) 

    os.rename(source_path, destination_path)
    print(f)

    current_file += 1

    if current_file >= max_files:
        current_file = 0
        page += 1



