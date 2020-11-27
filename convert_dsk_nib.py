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
import subprocess


def convert(dsk2nib_path, working_path, name, verbose = True):

    process = subprocess.Popen([dsk2nib_path + '/dsk2nib.exe', working_path + '/' + name + '.dsk', working_path + '/' + name + '.nib'], 
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        line = output.strip()
        if verbose and line != "":
            print(line)
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            if verbose:
                print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                line = output.strip()
                if verbose and line != "":
                    print(line)
            break
        

def execute(dsk2nib_path, working_path, verbose = True):

    if not path.isdir(dsk2nib_path):    
        print("Caminho para o dsk2nib.exe não encontrado.")
        
    if not path.exists(dsk2nib_path):
        print("dsk2nib.exe não encontrado.")
    
    if not path.isdir(working_path):
        print("Caminho para os arquivos não encontrado.")

    onlyfiles = [f for f in listdir(working_path) if isfile(join(working_path, f)) and f.lower().endswith(".dsk")]

    for f in onlyfiles:
        filename = f.lower()
        filename = filename[:-4]
        
        if verbose:
            print("------------")
        
        print("Convertendo: " + filename)
        
        convert(dsk2nib_path, working_path, filename, verbose)


def main(argv):
    help = 'Uso: convert_dsk_nib.py [-h help] [-e <caminho> caminho para o dsk2nib] [-w <caminho> caminho para os arquivos dsk] [-v verbose]'

    dsk2nib_path = os.getcwd()
    working_path = os.getcwd()
    verbose = False
    
    try:
        opts, args = getopt.getopt(argv,"he:w:v")
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print(help)
            sys.exit()  
        if opt == '-e':
            dsk2nib_path = arg
        if opt == '-w':
            working_path = arg
        if opt == '-v':
            verbose = True
        
    execute(dsk2nib_path, working_path, verbose)

if __name__ == "__main__":

    main(sys.argv[1:])
    print("+ done!")
