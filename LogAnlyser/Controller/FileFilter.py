import difflib
import os
from FileAnalysis import FileAnalysis

object_fileanalysis     =   FileAnalysis()

class FileFilter:

    def __init__(self,input_check) -> None:

        self._output_path_      =   object_fileanalysis._output_path_
        self._filtered_path_    =   "LogAnalyser/Output/Filter.log"
        self._loglines_path_    =   "LogAnalyser/Output/LogLines.log"
        self.input_check_p      =   "["+input_check+"]"
        self.counter            =   0  
        

    def applyingFilter(self):

        with open(self._output_path_,"r")  as f:
            _fileData_      =   f.readlines()
            for lin in _fileData_:
                if  self.input_check_p in lin:
                    file_array        = []
                    file_array.append(lin)
                    self.counter+=1
                    with open(self._loglines_path_ ,"a")  as ll:
                        ll.writelines(lin + "\n")
                    unspaced_lines    =    file_array[0].replace("     "," ")
                    piped_lines       =    unspaced_lines.replace(" ","|")
                    piped_lines       =    piped_lines.strip().split("|")
                    time_data         =    piped_lines[1:][0]+" "+piped_lines[1]
                    with open(self._filtered_path_,"a")  as fil:
                        fil.writelines(time_data + "\n")
        print("No of "+self.input_check_p+" Statements are : ["+str(self.counter)+"]")
