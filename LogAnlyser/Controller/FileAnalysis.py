class FileAnalysis():
    
    def __init__(self) -> None:
        # super.__init__()
        self._file_path__            =       "LogAnalyser/Model/DataLayer/x1.log"
        self._output_path_           =       "LogAnalyser/Output/Analysis.log"
        self._analysis_start         =       "End Display Current Environment"
        self.file_start              =        False

        
    '''
        --> Reading the lines.
        --> Find the string of line to analyse and start the analysis
    '''

    def fileAnlyser(self):
        with open(self._file_path__,"r")  as f:
            _fileData_      =   f.readlines()
            counter         =   0
            for i in _fileData_:
                line_split  =   _fileData_[counter].split("|")
                if self._analysis_start in line_split[0]:
                    xcounter    =   counter
                    self.fileAnlyseLines (_fileData_,xcounter)
                counter+=1

    '''
        --> This Function will start the counter by skiping the Unnecessary lines.
        --> Write all the Import Lines into the Analysis log.
        --> Adding Counter to Index the Lines
    '''

    def fileAnlyseLines (self,_fileData_,xcounter):
        test_counter    =   0
        self.xs_index   =   0
        for i in _fileData_[xcounter+1:]:
            with open(self._output_path_ ,"a")  as out:
                out.writelines("Index "+str(self.xs_index)+" "+ i)
            self.xs_index+=1
            test_counter+=1
            
