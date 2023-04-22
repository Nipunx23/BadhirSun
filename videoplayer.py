from tkinter import *
import datetime
import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo

root=tk.Tk()
root.title("𝕭𝖆𝖉𝖍𝖎𝖗 𝕾𝖚𝖓")
root.geometry("800x700+290+10")


frame =tk.Frame(root)
frame.pack()

image_icon = PhotoImage(file= "BadhirSunLogo.gif")
root.iconphoto(False,image_icon)

lower_frame = tk.Frame(root,bg="#FFFFFF")
lower_frame.pack(fill= "both" , side = BOTTOM)

load_btn = tk_Button(root, text = "Search",bg = "0B2447", font = ("impact" , 12, "bold" ),foreground = [('active', '!disabled' , 'black')],background = [('active' , 'white')] , command = lambda :  load_video)
loat_btn.pack(ipadx=12 , ipady=4, anchor = tk.NE)

vid_player = TkinterVideo(root, scaled = True)
vid_player.pack(expand = True, fill = "both")
root.mainloop()