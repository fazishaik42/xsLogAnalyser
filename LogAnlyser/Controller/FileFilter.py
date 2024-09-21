import difflib
import os
from FileAnalysis import FileAnalysis

object_fileanalysis     =   FileAnalysis()

class FileFilter:

    '''
        --> added kwargs to read input Seach string and Ignore String.
    '''

    def __init__(self,**kwargs) -> None:

        self._output_path_      =   object_fileanalysis._output_path_
        self._filtered_path_    =   "LogAnalyser/Output/Filter.log"
        self._loglines_path_    =   "LogAnalyser/Output/LogLines.log"
        self.input_check_p      =   "["+kwargs.get("accept")+"]"
        self.xs_ignore_search   =   "["+kwargs.get("ignore")+"]"
        self.counter            =   0  
    
    '''
        --> Method to extract the log statement based on the User criteria.
        --> Method to ignore the log statements based on the User criteria.
        --> If statement to Which will filter the log based on the Seach string and Ignore String.
    '''

    def applyingFilter(self):

        with open(self._output_path_,"r")  as f:
            _fileData_      =   f.readlines()
            for lin in _fileData_:
                if  (self.input_check_p in lin) or (self.xs_ignore_search not in lin):
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

    def no_of_statement(self):
        self.input_check_p  =   self.input_check_p.replace("[", "").replace("]", "")
        xs_msg=" "+str(self.counter)+" "+self.input_check_p+" Statements retrieved"
        return xs_msg
