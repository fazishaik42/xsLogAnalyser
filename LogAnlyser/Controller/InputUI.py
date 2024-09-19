from tkinter import *
import tkinter as tk
import tkinter.messagebox 
from FileFilter import FileFilter
from FileAnalysis import FileAnalysis
import time

class InputUI:

    '''
        --> write the **kwargs for the below __init__ method.
        --> **kwrgs should accept the button text, Command function.
    '''

    def __init__(self,**kwargs):
        self.main_screen          =   tk.Tk()

    '''
        --> The xs_Open Window Method is called to Set the ScreenSize.
        --> Accepts the String value from the Entry Window.
        --> Sets the Button to trigger the Analyser
        --> Arrange the Button onto the Grid
        --> Accepts the Input and process the file anaylis, & applies filefilter
    '''

    def xs_open_window(self,**kwargs):
        self.main_screen.geometry("600x400")
        self.main_screen.title("LogAnalyser")
        self.xs_input_var         =   tk.StringVar()
        self.name_label           =   tk.Label(self.main_screen, text = 'Statement Type ', font=('calibre',10, 'bold'))
        self.name_entry           =   tk.Entry(self.main_screen,textvariable = self.xs_input_var , font=('calibre',10,'normal'))
        self.sub_btn              =   tk.Button(self.main_screen,text = 'Start Analyser', command = self.xs_entry_func)
        self.name_label.grid(row=0,column=2)
        self.name_entry.grid(row=0,column=3)
        self.sub_btn.grid(row=2,column=3)
        self.main_screen.mainloop()

    '''
        --> This Function takes the Input from the screen & Passes the Input to a Function # pass_input()
    '''
    def xs_entry_func(self):
        x1                  =   self.name_entry.get()
        self.xs_newEntry    =   x1
        return self.pass_input(self.xs_newEntry)
    
    '''
        --> This Function creates a small pop-up message after completing the Txn.
    '''

    def xsSimpleMessage(self):
        self.root = tkinter.Tk() 
        self.root.geometry('500x300') 
        tkinter.messagebox.showinfo("LogAnalyser", "Success!") 
        # time.sleep(2)
        # self.root.destroy()
        # self.root.mainloop()
    
    def pass_input(self,Entry):

        '''
            --> Intialising the Objects of the Two classes.
            --> Adding an Input parameter for the User to select the Input parameter
        '''
        self.xs_file_filter  =   FileFilter(Entry.upper())
        self.xs_Object       =   FileAnalysis()

        '''
            --> The File Analyser will break the file and makes the file more readable in python.
        '''

        self.xs_Object.fileAnlyser()

        '''
            --> The FileFilter class filters the statements based on the Input parameter.
            --> After filtering the file, Seperates the respective Log statement in the LogLines file.
        '''

        self.xs_file_filter.applyingFilter()

        time.sleep(2)
 

        '''
            --> Close the Window after the Input is Passed
        '''

        self.main_screen.destroy()

        '''
            --> Display a Success Message after closing MainScreen Window.
        '''

        # self.xsSimpleMessage()
