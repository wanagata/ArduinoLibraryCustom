from os import getcwd,mkdir,path
import csv
from Inserttextfile import Inserttextfile 

class ArduinoLibraryCustom:
    def __init__(self):
        self.source_dir = getcwd()
        self.dummy = self.source_dir+"/Dammyfiles/"
        self.class_list = []

    def start(self,classes_csv_filename):
        #read csv file
        with open(classes_csv_filename,newline='') as f:
            reader = csv.reader(f)
            _list = list(reader)
            self.class_list = [lib_name[0] for lib_name in _list]
        print(self.class_list)
        ansd = input("Do you want to convert these "+ str(len(self.class_list)) + " classes(y/n) : ")
        if ansd != 'y':
            exit()
        self.generatefiles()
            
    def generatefiles(self):
        for library_name in self.class_list:
            TARGET_DIR = self.source_dir+"/"+library_name
            #print(TARGET_DIR)
            #create directory
            if path.exists(TARGET_DIR)!=True:
                mkdir(TARGET_DIR) 

            example_filename = library_name+"testing"
            #create library directory
            all_folder = ["/src","/examples","/examples/"+example_filename]
            all_folder = []
            for fol in all_folder:
                #create directory
                if path.exists(TARGET_DIR+fol)!=True:
                    mkdir(TARGET_DIR+fol) 
            
            #TARGET_DIR = TARGET_DIR+"/"

            #create keyword file
            #file = open(TARGET_DIR+"keywords.txt", "w")
            #file.write( library_name +"\tKEYWORD1\n")
            #file.write( "dash\tKEYWORD2\n")
            #file.write( "dot\tKEYWORD2\n")
            #file.close()

            code = library_name
            #create C++ file
            newtool = Inserttextfile()
            newtool.set_source(self.dummy+"dammy_cpp.txt")
            
            newtool.set_new_filename(TARGET_DIR+"/"+library_name+".cpp")
            newtool.insert_code(code)
            newtool.writefile()

            #create c library file
            newtool.set_source(self.dummy+"dammy_h.txt")
            newtool.set_new_filename(TARGET_DIR+"/"+library_name+".h")
            newtool.insert_code(code)
            newtool.writefile()

            #create example file
            newtool.set_source(self.dummy+"dammy_ino.txt")
            newtool.set_new_filename(TARGET_DIR+"/"+library_name+".ino")
            newtool.insert_code(code)
            newtool.writefile()

