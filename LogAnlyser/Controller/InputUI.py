from tkinter import *

from FileAnalysis import FileAnalysis

class InputUI:

    '''
        --> write the **kwargs for the below __init__ method.
        --> **kwrgs should accept the button text, Command function.
    '''

    def __init__(self,**kwargs):

        self.xs_button_func     =   FileAnalysis()
        self.xs_window          =   Tk()
        self.xs_window_button   =   Button(text=kwargs.get("text"), command=kwargs.get("func"))
        self.xs_window_button.pack()

    def xs_open_window(self):

        self.xs_window.title("Input Parameter : ")
        self.xs_window.minsize(width=500,height=500)
        self.xs_window.mainloop()
