from tkinter import*
# Tạo cửa sổ chính của ứng dụng GUI
root = Tk()
root.title("Atlab Data Logger Manage Tool")
root.iconbitmap('D:/icon/favicon.ico')
root.geometry("800x800")
root.maxsize(800, 800)
root.configure(background='grey')

#tạo khung chính
main_frame = Frame(root, width=790, height=790, bg="#353638")
main_frame.grid(row=1, column=0, padx=5, pady=5)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 0, weight=1)

root.mainloop()