from tkinter import *
root = Tk()
root.title("Mellody")
root.iconbitmap('D:/icon/favicon.ico')

def open():
    top = Toplevel()
    top.title('Setting')
    top.iconbitmap('D:/icon/favicon.ico')
btn=Button(root, text="setting", command=open).pack()
root.mainloop()