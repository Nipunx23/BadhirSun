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

image_icon = PhotoImage(file= "images\BadhirSunLogo.gif")
root.iconphoto(False,image_icon)

lower_frame = tk.Frame(root,bg="#FFFFFF")
lower_frame.pack(fill= "both" , side = BOTTOM)

load_btn = tk_Button(root, text = "Search",bg = "0B2447", font = ("impact" , 12, "bold" ),foreground = [('active', '!disabled' , 'black')],background = [('active' , 'white')] , command = lambda :  load_video)
loat_btn.pack(ipadx=12 , ipady=4, anchor = tk.NE)

vid_player = TkinterVideo(root, scaled = True)
vid_player.pack(expand = True, fill = "both")

Button_bckwrd = PhotoImage(file="images\backward button.png")
backb = tk.Button(lower_frame,image=Button_bckwrd , bd=0 ,height=50 , width = 50 , command = lambda:skip(-5)).pack(side = LEFT)

Button_pp = PhotoImage(file="images\pp_button.jpg")
play_pause_btn = tk.Button(lower_frame , image= Button_pp, bd=0 ,height=50, width=50 , command = play_pause)
play_pause_btn.pack(expand = True,fill = "both" , side = LEFT)

Button_frwrd = PhotoImage(file="images\forward button.png")
backf = tk.Button(lower_frame,image=Button_frwrd , bd=0 ,height=50 , width = 50 , command = lambda:skip(5)).pack(side = RIGHT)

root.mainloop()