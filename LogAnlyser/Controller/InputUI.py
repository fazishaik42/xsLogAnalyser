from tkinter import *
import tkinter.messagebox 
from FileFilter import FileFilter
from FileAnalysis import FileAnalysis
import time
import customtkinter as ctk
import customtkinter as ctkx
from pathlib import Path
from GenAIRequestHandler import GenAIRequestHandler



class InputUI:

    '''
        --> Imported the customtkinter module for better looking UI Design. 
        --> Sets the Window them based on the System
        --> Sets the default color theme.
    '''

    ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  

    '''
        --> write the **kwargs for the below __init__ method.
        --> **kwrgs should accept the button text, Command function.
    '''

    def __init__(self) :

        '''
            --> Setting up the root Screen.
            --> Set the size of the Window.
        '''
        self.main_screen   =   ctk.CTkToplevel()
        self.main_screen.geometry("1280x720")
        self.main_screen.title("LogAnalyser")
        self.xs_frame               =   ctk.CTkFrame(master=self.main_screen)
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
        self.name_label           =   ctk.CTkLabel(master=self.xs_frame, text = '    Maximo Log Analysis', font=('calibre',15, 'bold'))
        self.entry_label          =   ctk.CTkLabel(master=self.xs_frame, text = 'Search For', font=('calibre',10, 'bold'))
        self.name_entry           =   ctk.CTkEntry(master=self.xs_frame,textvariable = self.xs_input_var , font=('calibre',10,'normal'))
        self.ignore_label         =   ctk.CTkLabel(master=self.xs_frame, text = 'Ignore Statement of', font=('calibre',10, 'bold'))
        self.ignore_entry         =   ctk.CTkEntry(master=self.xs_frame,textvariable = self.xs_ignore_var , font=('calibre',10,'normal'))
        self.sub_btn              =   ctk.CTkButton(master=self.xs_frame,text = 'Start Analyser', command = kwargs["func"])
        self.sub_cls              =   ctk.CTkButton(master=self.xs_frame,text = 'Close Analyser', command = kwargs["cls"])
        self.name_label.grid(row=0,   column=4)
        self.entry_label.grid(row=1,  column=1)
        self.name_entry.grid(row=1,   column=2)
        self.ignore_label.grid(row=1, column=3)
        self.ignore_entry.grid(row=1, column=4)
        self.sub_btn.grid(row=1,      column=5)
        self.sub_cls.grid(row=1,      column=6)
        for widget in self.xs_frame.winfo_children():
            widget.grid_configure(padx=5,pady=5)
        self.xs_frame.pack(padx=10,pady=10)
        self.main_screen.mainloop()

    '''
        --> Function to close the main screen windo
    '''
    def cls(self):
        self.main_screen.destroy()

    '''
        --> This Method takes the Input from the screen & Passes the Input to a Function # pass_input()
        --> This Method passes the Input and store thems in an array.
    '''

    def xs_entry_func(self):
        if self.name_entry.get()==None or self.name_entry.get()=='':
            self.xsSimpleMessage(xs_msg="Please provide a Search String ?")

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

    def xs_ask_askokcancel(self,msg):
        self.root           =   tkinter.Tk() 
        self.root.geometry('500x300')
        xs_ok_to_cancel     =   tkinter.messagebox.askokcancel("askokcancel", msg) 
        return xs_ok_to_cancel
    
    def removeOutputfiles(self):
        root_folder         =   Path(self.xs_Object.xs_root_dir)
        print(f"Path to Output Folder:{root_folder}")
        for f in root_folder.iterdir():
            try:
                if f.is_file():
                    f.unlink()
                    print(f"Deleted Files as per user Input :{f}")
            except Exception as e:
                print(f"Error deleting file {f} : {e}")

    '''
        --> Function return the response that is generated from the AI.
    '''
    def xsCheckAIResp(self):
        with open(self.xs_file_filter.xs_AI_resp,'r') as ai_Resp:
            ai_Resp_data      =   ai_Resp.readlines()
            for ai in ai_Resp_data:
                try:
                    ai_txt            =   ""
                    ai_txt            +=  ai
                finally:
                    # self.xs_gem_val.insert(ctk.END, ai_txt)
                    pass
                return ai_txt
            
    '''
        --> Function opens a New Window to access the AI Response.
    '''        
    def open_new_window(self,**kwargs):
        self.AI_screen   =   ctkx.CTkToplevel(self.main_screen)
        self.AI_screen.geometry("1280x720")
        self.AI_screen.title("LogAnalyser")
        self.xs_AI_frame             =   ctkx.CTkFrame(master=self.AI_screen)
        self.xs_AI_frame.pack(pady=10,padx=10)
        xs_AI_name_label          =   ctkx.CTkLabel(master=self.xs_AI_frame, text = 'Responses from the GEMINI AI', font=('calibre',15, 'bold'))
        self.resp_btn             =   ctkx.CTkButton(master=self.xs_AI_frame,text = 'AI Response',command=kwargs.get("func"))
        self.Ai_Close             =   ctkx.CTkButton(master=self.xs_AI_frame,text = 'Close',command=kwargs.get("Close"))
        xs_AI_name_label.grid(row=0,column=0)
        self.resp_btn.grid(row=0,column=1)
        self.Ai_Close.grid(row=0,column=2)
        xs_txt_frame             =   ctkx.CTkFrame(master=self.AI_screen)
        self.xs_gem_val          =   ctkx.CTkTextbox(master=xs_txt_frame,width=1024,height=768,corner_radius=5)
        self.xs_gem_val.grid(row=0,column=0)
        self.xs_gem_val.pack(padx=5,pady=5)
        xs_txt_frame.pack(pady=10,padx=10)
        for widget in self.xs_AI_frame.winfo_children():
            widget.grid_configure(padx=5,pady=5)
        self.xs_AI_frame.pack(padx=10,pady=10)
        self.AI_screen.mainloop()

    '''
        --> New window that is opened as part of the AI response, The below function will close the AI response.
    '''
    def windowDestroy(self):
        self.AI_screen.destroy()

    '''
        --> Function that Return the AI Response in the Text Window.
    
    '''

    def xs_AI_func(self):
        print("Button Clicked")
        self.xs_AI_Instance  =   FileFilter(accept="ERROR",ignore="INFO")
        with open(self.xs_AI_Instance.xs_AI_resp,'r') as ai_Resp:
            ai_Resp_data      =   ai_Resp.readlines()
            for ai in ai_Resp_data:
                try:
                    ai_txt            =   ""
                    ai_txt            +=  ai
                finally:
                    self.xs_gem_val.insert(ctkx.END, ai_txt)

    '''
        --> Timer function
        --> Timer function will open a windows for 30 seconds and starts the timer for 30 sec
    '''

    def xs_open_timer(self):
        self.win = ctkx.CTkToplevel()
        self.win.geometry("300x300")
        self.xs__timer_label    =   ctkx.CTkLabel(master=self.win, text = 'Responses from the GEMINI AI', font=('calibre',10, 'bold'))
        self.xs__timer_label.grid(row=0,column=0)
        self.xs__timer_label.pack(padx=5,pady=5)
        index = 15
        start_timer = True
        while start_timer:
            self.xs__timer_label.configure(text="Awaiting Response from AI... "+str(index))
            self.xs__timer_label.after(1000)
            self.xs__timer_label.update()
            index -= 1
            if index < 1:
                start_timer = False
            else:
                start_timer = True
        self.win.destroy()
        self.win.mainloop()

              
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
            --> Display a Success Message after closing MainScreen Window.
        '''

        self.xsSimpleMessage(obj=self.xs_file_filter)


        '''
            --> Call the AI Class starting from here.
            --> Generates a file for AI Response.
            -->Triggers GenAIRequestHandler class file.
            --> Ask the user to check the with Gemini for responses.

        '''
        xs_AI           =   GenAIRequestHandler()

        xs_AI.xsRequestAI()      

        '''
            --> Call the New Window here. 
            --> Call this method to check the response on screen.
            --> Screen Sizes:
                    - 800x600(4:3)
                    - 1024x768(4:3)
                    - 1152x864(4:3)
                    - 1280x960(4:3)
                    - 1280x720(16:9)
                    - 1920x1080(16:9)
                    - 2560x1440(16:9)
                    - 3840x2160(16:9)
                    - 1280x800(16:10)
                    - 1920x1200(16:10)
                    - 2560x1600(16:10)
                    - 2880x1800(16:10)
            --> xs_AI_screen
                    - xs_AI_frame
                        - xs_AI_name_label
                    - xs_txt_frame
                        - xs_gem_val                                               
        '''
        self.open_new_window(func=self.xs_AI_func,Close=self.windowDestroy)

        '''
            --> Close the Window after the Input is Passed
        '''
        
        self.main_screen.destroy()
