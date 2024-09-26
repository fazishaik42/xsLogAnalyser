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
        self.xs_log_prep        =   "LogAnalyser/Output/Logprep.log"
        self.xs_AI_resp         =   "LogAnalyser/Output/Gemini Resp.log"
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
    
    '''
        --> This method returns the segregated ERROR statement to AI request Handler.
        --> This method return the statements in the form of List.
        --> This method ignores the WARN Statements

    '''

    def readErrorStatement(self):

        with open(self._loglines_path_,"r") as err:
            xs_error_data       =   err.readlines()
            xs_error_holder     =   []
            xs_traceHolder      =   []
            xs_container        =   []
            xs_ignore_war       =   "[WARN]"    
            for er in xs_error_data:
                if (self.input_check_p in er) and (xs_ignore_war not in er):
                    xs_error_holder.append(er)
                else:
                    xs_traceHolder.append(er)
            xs_container.append(xs_error_holder)
            xs_container.append(xs_traceHolder)
            with open(self.xs_log_prep ,'a')  as xs_lp:
                xs_ai_reqBody   =   []
                for x in range(0,len(xs_container[0])):
                    xs_lp.write(str(xs_container[0][x]))
                    if  self.input_check_p  in str(xs_container[0][x]):
                        xs_Ai_body     =  {
                                "contents": [
                                    {
                                        "parts": [
                                            {
                                                "text": "Analysing the Maximo Log, Gave me this errored Log statements. Analyse this log statatement and rate this error on a scale of 1 to 5 where 1 being the critical. Please provide necessary solotion steps as well. Error starts from here :  "+ xs_container[0][x] 
                                            }
                                        ]
                                    }
                                ]
                            }
                        xs_ai_reqBody.append(xs_Ai_body)

                return xs_ai_reqBody

                '''
                        --> The below commented statement can generate the Stack trace this stack trace, is not necessary at this point in time.
                        --> Just analysing the high level error statements.
                '''
                        # for y in range(0,len(xs_container[1])):
                        #     xs_lp.write(str(xs_container[1][y]))
    '''
        --> Writes the AI Response to a log File.
        --> Receives the Input data from AI Response.
    '''
    def xsWriteAIResponse(self,data):
        with open(self.xs_AI_resp,'a') as resp:
            resp.write(data)
            resp.write("========================================================== \n")
