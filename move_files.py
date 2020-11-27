#!/usr/bin/env python
""" Short description of this Python module.
Longer description of this module.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Augusto Baffa"
__contact__ = "augusto@baffasoft.com.br"
__copyright__ = "Copyright 2020, Baffasoft"
__credits__ = ["Augusto Baffa", "Baffasoft"]
__date__ = "2020/11/27"
__deprecated__ = False
__email__ =  "augusto@baffasoft.com.br"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.2"

import os,sys,inspect, getopt
from os import listdir, path
from os.path import isfile, join


def count_files(dir):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f)) and f != os.path.basename(__file__)]
    return len(onlyfiles)


def check_folder(page, working_path, max_files, verbose):

    dir_name = "dir%02d" % page
    dir_path = working_path + "/" + dir_name
    
    if not path.exists(dir_path):
        if verbose:
            print("+ Criando Diretório: " + dir_name)
        os.mkdir(dir_path)
        current_file = 0
    else:
        while path.exists(dir_path) and count_files(dir_path) >= max_files:
            page += 1            
            dir_name = "dir%02d" % page
            dir_path = working_path + "/" + dir_name
            if verbose:
                print("+ Diretório estava cheio, tentando: " + dir_name)

        if not path.exists(dir_path):
            if verbose:
                print("+ Criando Diretório: " + dir_name)
            os.mkdir(dir_path)                 
            current_file = 0
        else:
            current_file = count_files(dir_path)
            if verbose:
                print("+ Diretório Atual: " + dir_name + " com %d arquivo(s)." % current_file)
                
    return dir_name, dir_path, page, current_file


def execute(working_path, verbose = True):
    
    if not path.isdir(working_path):
        print("Caminho para os arquivos não encontrado.")


    onlyfiles = [f for f in listdir(working_path) if isfile(join(working_path, f)) and f != os.path.basename(__file__)]

    if len(onlyfiles) == 0:
        print("Nenhum arquivo encontrado para organização.")
    elif len(onlyfiles) == 1:
        print("Encontrei 1 arquivo para organização.")
    else:
        print("Foram encontrados %d arquivos para organização." % len(onlyfiles))
    
    print()

    
    max_files = 125
    
    page = 1
    dir_name, dir_path, page, current_file = check_folder(page, working_path, max_files, verbose)

    for f in onlyfiles:

        source_path =  working_path + "/" + f
        destination_path = dir_path + "/" + f

        os.rename(source_path, destination_path)
        if verbose:
            print("Movendo arquivo " + f)

        current_file += 1

        if current_file >= max_files:
            dir_name, dir_path, page, current_file = check_folder(page + 1, working_path, max_files, verbose)


def main(argv):
    help = 'Uso: move_files.py [-h help] [-w <caminho> caminho para os arquivos] [-v verbose]'

    working_path = os.getcwd()
    verbose = False
    
    try:
        opts, args = getopt.getopt(argv,"hw:v")
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print(help)
            sys.exit()  
        if opt == '-w':
            working_path = arg
        if opt == '-v':
            verbose = True
        
    execute(working_path, verbose)

if __name__ == "__main__":

    main(sys.argv[1:])
    print("+ done!")


