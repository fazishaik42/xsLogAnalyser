import requests

from FileFilter import FileFilter

'''
    --> API Key generated from https://console.cloud.google.com/apis/credentials
    --> Generate your API KEY from your google account and Update the String Value below.
'''

API_KEY         =       ""

'''
    --> URL to Post the Request.
'''

GEN_AI_URL      =       "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key="


class GenAIRequestHandler:

    def __init__(self) -> None:
        pass

    
    '''
        --> Initiates the AI request
    '''

    def xsRequestAI(self,**kwargs):
      
        '''
                --> Create a request for Gemini with Json Build Parameter.
                --> Always Intialise file filter Object.
        '''
        xs_file_filter_obj       =   FileFilter(accept="ERROR",ignore="INFO")

        '''
            --> Function to print the container list which is holding the error statements from the Log.
            --> This function will contain the error and respective stacktraces in the form of arrays.
            --> Loop through the list of Arrays and request for AI Support.
        '''
      
        xs_ai_promot             =   xs_file_filter_obj.readErrorStatement()
        print(f"No of error Statement to send to AI : " + str(len(xs_ai_promot)))
        for i in range(0,len(xs_ai_promot)):
            response    = requests.post(GEN_AI_URL + API_KEY,json=xs_ai_promot[i])
            if response.status_code == 200:
                data = response.json()
                xs_AI_RESP  =   data["candidates"][0]["content"]["parts"][0]["text"].replace("**","")
                xs_file_filter_obj.xsWriteAIResponse(data=xs_AI_RESP)
            else:
                print("Response : " + str(response))
                print("Error:", response.status_code)

