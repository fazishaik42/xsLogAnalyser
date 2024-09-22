
from InputUI import InputUI
from GenAIRequestHandler import GenAIRequestHandler

xs_is_start     =   True

while xs_is_start:

    '''
        --> Adding the UI Elements from this section.
        --> The below InputUI class is Initialised with a window.
        --> This class will create the starting window of the Project.
        --> Developer can write the Event trigger for the button.
        --> Import the class from which the button should trigger the function.
        --> Intialise the button with the event of the function.
        --> Now the InputUI object takes the **kwargs

    '''
    xs_input_ui     =   InputUI()

    '''
        --> The xs_Open Window Method is called to Set the ScreenSize.
        --> Accepts the String value from the Entry Window.
        --> Sets the Button to trigger the Analyser
        --> Arrange the Button onto the Grid
        --> Accepts the Input and process the file anaylis, & applies filefilter
        --> Accepts the Input to search and also accepts the Input to ignore.
    '''

    xs_input_ui.xs_open_window(func=xs_input_ui.xs_entry_func)


    '''
        --> Generates a file for AI Response.
        -->Triggers GenAIRequestHandler class file.
        --> Ask the user to check the with Gemini for responses.
    '''
    if xs_input_ui.xs_ask_askokcancel(msg="Check Gemini AI Response for Log Analysis?"):

        xs_AI           =   GenAIRequestHandler()

        xs_AI.xsRequestAI()

        if xs_input_ui.xs_ask_askokcancel(msg="Want to Continue?"):

            '''
                --> Getting Exception when reinitialising 
            '''
            if xs_input_ui.xs_ask_askokcancel(msg="System will remove the logs of Old Analysis"):
                xs_input_ui.removeOutputfiles()

            xs_is_start     =   False
            # xs_input_ui.main_screen.destroy()

        else:
            xs_is_start     =   False
            xs_input_ui.xsSimpleMessage(xs_msg="Application is Closing.")
    else:
        xs_is_start     =   False
        xs_input_ui.xsSimpleMessage(xs_msg="Application is Closing.")
