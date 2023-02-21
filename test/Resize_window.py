from tkinter import*
# Tạo cửa sổ chính của ứng dụng GUI
root = Tk()
root.title("Atlab Data Logger Manage Tool")
root.geometry("500x500")
root.configure(background='grey')

#tao nut button
button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")

#tao grid cho man hinh
button_1.grid(row=0, column=0, sticky="nsew")
button_2.grid(row=1, column=0, sticky="nsew")

#resize buttons when resize a window
button_list = [button_1, button_2]
row_number = 0
for button in button_list:
    Grid.rowconfigure(root, row_number, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    row_number +=1



root.mainloop()