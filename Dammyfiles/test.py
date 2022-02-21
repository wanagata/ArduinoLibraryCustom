
from os import listdir,getcwd,mkdir,path

import fileinput
code = "Morse"
for line in fileinput.FileInput(getcwd()+"\Dammyfiles\dammy_cpp.txt",inplace=1):
    if '$' in line:
        #split with $
        x = line.split('$')
        newline = ""
        
        for i,txt in enumerate(x):
            newline = newline + txt 
            if '\n' not in txt: #check for final word
                newline = newline + code
                pass
            pass
        pass
        line = newline
