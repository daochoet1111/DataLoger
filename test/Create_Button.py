from tkinter import *

root = Tk()  # create parent window
root.geometry("200x200")
root.maxsize(800, 800)
volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+")
vol_up.pack()

vol_down = Button(root, text="-")
vol_down.pack()

root.mainloop()