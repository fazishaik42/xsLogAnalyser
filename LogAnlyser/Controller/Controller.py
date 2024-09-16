import difflib
import os
from FileAnalysis import FileAnalysis
from FileFilter import FileFilter

'''
    --> Intialising the Objects of the Two classes.
'''
xs_Object       =   FileAnalysis()

xs_file_filter  =   FileFilter()

'''
    --> The File Analyser will break the file and makes the file more readable in python.
'''

xs_Object.fileAnlyser()

xs_file_filter.applyingFilter()
