import difflib
import os
from FileAnalysis import FileAnalysis
from FileFilter import FileFilter
import tkinter
from InputUI import InputUI



'''
    --> Intialising the Objects of the Two classes.
    --> Adding an Input parameter for the User to select the Input parameter
'''
xs_Object       =   FileAnalysis()

input_check     =   input("Enter the Input Parameter : ")

xs_file_filter  =   FileFilter(input_check.upper())



'''
    --> The File Analyser will break the file and makes the file more readable in python.
'''

xs_Object.fileAnlyser()

'''
    --> The FileFilter class filters the statements based on the Input parameter.
    --> After filtering the file, Seperates the respective Log statement in the LogLines file.
'''
xs_file_filter.applyingFilter()

xs_input_ui     =   InputUI()

xs_input_ui.xs_open_window()
