import tkinter as tk
import ctypes as ct


def dark_title_bar(window):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),4)

root = tk.Tk()
root.title("Crystaly Ball")
root.geometry("1400x900")
root.configure(background="#222246")
dark_title_bar(root)
root.mainloop()