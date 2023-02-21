from tkinter import *
import Button_list 

root = Tk()  # create parent window
root.geometry("200x200")
root.maxsize(800, 800)
volume = Label(root, text="VOLUME")
volume.pack()

#import class in main

object = Button_list.Buttonlist("len", "Button_1")


#x = object("len", "Button_1")


root.mainloop()