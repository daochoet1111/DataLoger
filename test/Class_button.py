from tkinter import *

root = Tk()  # create parent window
root.geometry("200x200")
root.maxsize(800, 800)
volume = Label(root, text="VOLUME")
volume.pack()

class Buttonlist:
  def __init__(self, vol_up, text_button):
    self.text_button = text_button
    vol_up = Button(root, text=text_button)
    vol_up.pack()


x = Buttonlist("len", "Button_1")
y = Buttonlist("nut2", "Button 2")
x = Buttonlist("len", "Button_1")
y = Buttonlist("nut2", "Button 2")
root.mainloop()