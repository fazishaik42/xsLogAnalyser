from tkinter import *
import tkinter as tk
class InputUI:

    '''
        --> write the **kwargs for the below __init__ method.
        --> **kwrgs should accept the button text, Command function.
    '''

    main_screen          =   tk.Tk()

    def __init__(self):
        
        self.main_screen.geometry("600x400")
        # self.xs_button_func     =   FileAnalysis()
        # self.xs_window          =   Tk()
        # self.xs_window_button   =   Button(text=kwargs.get("text"), command=kwargs.get("func"))
        # self.xs_window_button.pack()

    def xs_open_window(self,**kwargs):
        self.xs_window          =   Tk()
        self.xs_window.title("LogAnalyser")
        self.xs_window.minsize(width=500,height=500)
        self.xs_window_button   =   Button(text=kwargs.get("text"), command=kwargs.get("func"))
        self.xs_window_button.pack()

        self.xs_window.mainloop()

    def xs_entry_func(self):
        x1  =   self.xs_input
        return x1
    
    main_screen.mainloop()
