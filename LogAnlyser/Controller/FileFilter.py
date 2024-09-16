import difflib
import os
from FileAnalysis import FileAnalysis

object_fileanalysis     =   FileAnalysis()

class FileFilter:

    def __init__(self) -> None:

        self._output_path_      =   object_fileanalysis._output_path_

        self._filtered_path_    =   "LogAnalyser/Output/Filter.log"

        self._loglines_path_    =   "LogAnalyser/Output/LogLines.log"

        self._look_up           =   ['[INFO]','[WARN]','[ERROR]']

    def applyingFilter(self):

        with open(self._output_path_,"r")  as f:

            _fileData_      =   f.readlines()

            for lin in _fileData_:

                for i in range(0,len(self._look_up)):

                    if self._look_up[i] in lin:

                        file_array        = lin.strip().split(self._look_up[i])

                unspaced_lines    =    file_array[0].replace("     "," ")

                piped_lines       =    unspaced_lines.replace(" ","|") # this log will be used for timestamp retrival

                # piped_lines       =    piped_lines.split("|")

                # if len(file_array)==2:

                #     log_lines         =    file_array[1]

                # else:

                #     log_lines         =    file_array[0]

                #     print(log_lines)

                with open(self._filtered_path_,"a")  as fil:

                    fil.writelines(piped_lines + "\n")

                # with open(self._loglines_path_ ,"a")  as ll:

                #     ll.writelines(log_lines+"\n")

                
