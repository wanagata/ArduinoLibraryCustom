import fileinput

class Inserttextfile():
    def __init__(self):
        self.code = ""
        self.txt = ""
        self.source_filename = ""
        self.new_filename = ""

    def set_source(self,source_filename):
        self.source_filename = source_filename

    def set_new_filename(self,new_filename):
        self.new_filename = new_filename

    def insert_code(self,code):    
        newtxt = ""
        for line in fileinput.FileInput(self.source_filename,inplace=0):
            if '$' in line:
                newline = ""
                for txt in line.split('$'): #split with $
                    newline = newline + txt 
                    if '\n' not in txt: #check for final word
                        newline = newline + code
                        pass
                    pass
                newtxt = newtxt + newline
            else:
                newtxt = newtxt + line
        self.txt = newtxt        
    
    def writefile(self):
        file = open(self.new_filename, "w")
        file.write(self.txt)
        file.close()
