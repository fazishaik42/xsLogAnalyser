
from InputUI import InputUI

'''
    --> Adding the UI Elements from this section.
    --> The below InputUI class is Initialised with a window.
    --> This class will create the starting window of the Project.
    --> Developer can write the Event trigger for the button.
    --> Import the class from which the button should trigger the function.
    --> Intialise the button with the event of the function.
    --> Now the InputUI object takes the **kwargs

'''

xs_input_ui     =   InputUI(reset=False)


'''
    --> The xs_Open Window Method is called to Set the ScreenSize.
    --> Accepts the String value from the Entry Window.
    --> Sets the Button to trigger the Analyser
    --> Arrange the Button onto the Grid
    --> Accepts the Input and process the file anaylis, & applies filefilter
'''

xs_input_ui.xs_open_window(func=xs_input_ui.xs_entry_func)

'''
    --> To restart the Application based on user Input.
'''

if xs_input_ui.xs_ask_askokcancel():
    '''
        --> Getting Exception when reinitialising 
    '''
    xs_input_ui_two =   InputUI(reset=True)
    xs_input_ui_two.xs_open_window(func=xs_input_ui.xs_entry_func)
else:
    xs_input_ui.xsSimpleMessage(xs_msg="Application is Closing.")
