from tkinter import *
import tkinter.messagebox 
from FileFilter import FileFilter
from FileAnalysis import FileAnalysis
import time
import customtkinter as ctk

class InputUI:

    '''
        --> Imported the customtkinter module for better looking UI Design. 
        --> Sets the Window them based on the System
        --> Sets the default color theme.
    '''

    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  

    '''
        --> write the **kwargs for the below __init__ method.
        --> **kwrgs should accept the button text, Command function.
    '''

    def __init__(self,**kwargs):
        
        '''
            --> Setting up the root Screen.
            --> Set the size of the Window.
        '''
        self.main_screen          =   ctk.CTk()
        self.main_screen.geometry("300x300")
        self.main_screen.title("LogAnalyser")
        self.xs_frame             =   ctk.CTkFrame(master=self.main_screen)
        self.xs_frame.pack(pady=10,padx=10)

    '''
        --> The xs_Open Window Method is called to Set the ScreenSize.
        --> Accepts the String value from the Entry Window.
        --> Sets the Button to trigger the Analyser
        --> Arrange the Button onto the Grid
        --> Accepts the Input and process the file anaylis, & applies filefilter
        --> Added Label for "Search String" & "Ignore String"
    '''

    def xs_open_window(self,**kwargs):
        self.xs_input_var         =   ctk.StringVar()
        self.xs_ignore_var        =   ctk.StringVar()
        self.name_label           =   ctk.CTkLabel(master=self.xs_frame, text = 'Maximo Log Analysis', font=('calibre',15, 'bold'))
        self.name_label.pack(pady=10, padx=10)
        self.entry_label          =   ctk.CTkLabel(master=self.xs_frame, text = 'Search For', font=('calibre',10, 'bold'))
        self.entry_label.pack(pady=10, padx=0)
        self.name_entry           =   ctk.CTkEntry(master=self.xs_frame,textvariable = self.xs_input_var , font=('calibre',10,'normal'))
        self.name_entry.pack(pady=0, padx=0)
        self.ignore_label         =   ctk.CTkLabel(master=self.xs_frame, text = 'Ignore Statement of', font=('calibre',10, 'bold'))
        self.ignore_label.pack(pady=10, padx=0)
        self.ignore_entry         =   ctk.CTkEntry(master=self.xs_frame,textvariable = self.xs_ignore_var , font=('calibre',10,'normal'))
        self.ignore_entry.pack(pady=0, padx=0)
        self.sub_btn              =   ctk.CTkButton(master=self.xs_frame,text = 'Start Analyser', command = kwargs["func"])
        self.sub_btn.pack(pady=10, padx=10)
        self.main_screen.mainloop()

    '''
        --> This Method takes the Input from the screen & Passes the Input to a Function # pass_input()
        --> This Method passes the Input and store thems in an array.
    '''

    def xs_entry_func(self):
        self.x1                      =   self.name_entry.get()
        self.x2                      =   self.ignore_entry.get()
        self.x3                      =   []
        self.x3.append(self.x1)
        self.x3.append(self.x2)
        return self.pass_input(self.x3)
    
    '''
        --> This Function creates a small pop-up message after completing the Txn.
        --> Fix the Icon Problem.
    '''

    def xsSimpleMessage(self,**kwargs):
        self.root = tkinter.Tk() 
        self.root.geometry('500x300')
        if kwargs.get("xs_msg")==None:
            tkinter.messagebox.showinfo(title="", message=kwargs.get("obj").no_of_statement())
        else:
            tkinter.messagebox.showinfo(title="", message=kwargs.get("xs_msg"))
        self.root.destroy()

    def xs_ask_askokcancel(self):
        self.root           =   tkinter.Tk() 
        self.root.geometry('500x300')
        xs_ok_to_cancel     =   tkinter.messagebox.askokcancel("askokcancel", "Want to continue?") 
        return xs_ok_to_cancel
    
    
    def pass_input(self,x3):

        '''
            --> Intialising the Objects of the Two classes.
            --> Adding an Input parameter for the User to select the Input parameter
            --> Intialises the FileFilter class with both "Search String" & "Ignore String"
        '''
        self.xs_file_filter  =   FileFilter(accept=x3[0].upper(),ignore=x3[1].upper())
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

        time.sleep(1)
 

        '''
            --> Close the Window after the Input is Passed
        '''

        self.main_screen.destroy()

        '''
            --> Display a Success Message after closing MainScreen Window.
        '''

        self.xsSimpleMessage(obj=self.xs_file_filter)
