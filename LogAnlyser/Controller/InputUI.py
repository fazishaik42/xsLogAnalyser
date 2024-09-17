import tkinter

class InputUI:
    
    def __init__(self):
        
        self.xs_window  =   tkinter.Tk()

    def xs_open_window(self):

        self.xs_window.title("Input Parameter : ")
        self.xs_window.minsize(width=500,height=500)
        self.xs_window.mainloop()
