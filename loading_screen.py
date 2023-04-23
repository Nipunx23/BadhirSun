import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from threading import Thread
import time

def dummy_func():
    # Put your backend function here
    # This is just a dummy example
    for i in range(100):
        print(i)
        time.sleep(0.1)
    return "Done!"

def show_loading_window():
    loading_window = tk.Toplevel()
    loading_window.title("Loading...")
    loading_window.geometry("200x100")
    ttk.Label(loading_window, text="Loading...").pack()
    ttk.Progressbar(loading_window, mode="indeterminate").pack(pady=10)
    return loading_window

def do_work():
    loading_window = show_loading_window()
    search_term = entry.get()

    def background_task():
        result = dummy_func()
        loading_window.destroy()
        showinfo("Result", result)

    thread = Thread(target=background_task)
    thread.start()

root = tk.Tk()
root.geometry("300x200")
root.title("Loading Window Example")

ttk.Label(root, text="Enter a search term:").pack(side="top")

entry = ttk.Entry(root)
entry.pack(side="top")

radio_youtube = ttk.Radiobutton(root, text="Search in YouTube", variable=tk.IntVar(), value=0)
radio_youtube.pack(side="top")

radio_system = ttk.Radiobutton(root, text="Search in System", variable=tk.IntVar(), value=1)
radio_system.pack(side="top")

ttk.Button(root, text="Search", command=do_work).pack(side="top", pady=10)

root.mainloop()
