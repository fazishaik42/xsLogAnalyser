class FileAnalysis:
    
    def __init__(self) -> None:
        
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
    '''

    def fileAnlyseLines (self,_fileData_,xcounter):
        
        test_counter    =   0

        for i in _fileData_[xcounter+1:]:

            with open(self._output_path_ ,"a")  as out:

                out.writelines(i)

            test_counter+=1
