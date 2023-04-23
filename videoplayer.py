from tkinter import *
import datetime
from ffpyplayer.player import MediaPlayer
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

vid_player: TkinterVideo = TkinterVideo(root, scaled = True)
vid_player.pack(side=LEFT, expand = True, fill = "both")
vid_player1: TkinterVideo = TkinterVideo(root, scaled = True)
vid_player1.pack(side=LEFT, expand = True, fill = "both")


def update_duration(event):
     duration = vid_player.video_info()["duration"]

     end_time["text"] = str(datetime.timedelta(seconds = duration))
     progress_slider["to"] = duration

def update_scale(event):
    progress_value.set(vid_player.current_duration())

def load_video():
     file_path = filedialog.askopenfilename()
     file_path1 = filedialog.askopenfilename()
     if file_path:
         vid_player.load(file_path)
         vid_player1.load(file_path1)
         progress_slider.config(to =0, from_ =0)
         play_pause_btn["text"] = "play"
         progress_value.set(0)


def seek(value):
    vid_player.seek(int(value))
    vid_player1.seek(int(value))

def skip(value:int):
    vid_player.seek(int(progress_slider.get())+value)
    vid_player1.seek(int(progress_slider.get()) + value)
    progress_value.set(progress_slider.get()+value)

def play_pause():
    if vid_player.is_paused():
        vid_player.play()
        vid_player1.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        vid_player1.pause()
        play_pause_btn["text"] = "play"


def video_ended(event):
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)

start_time = tk.Label(lower_frame, text = str(datetime.timedelta(seconds =0)))
start_time.pack(side = "left")

progress_value = tk.IntVar(root)

progress_slider = tk.Scale(lower_frame, variable=progress_value, from_=0, to=0, orient="horizontal", command=seek)
progress_slider.pack(side = "left" , fill = "x" , expand = True)

end_time = tk.Label(lower_frame, text = str(datetime.timedelta(seconds =0)))
end_time.pack(side = "left")

vid_player.bind("<<Duration>>")
vid_player1.bind("<<Duration>>")

#BUTTONS
load_btn = tk.Button(lower_frame, text="Load File", background="#DAF5FF", foreground="#0B2447", font=("Ysabeau-VariableFont_wght.ttf", 12, "bold"), command=lambda: load_video())
load_btn.pack(ipadx=12 , ipady=4, anchor = tk.NW)

Button_bckwrd = PhotoImage(file="backward button.png")
backb = tk.Button(lower_frame,image=Button_bckwrd , bd=0 , width=50 , height=50 , command = lambda:skip(-5)).pack(side = LEFT)

play_pause_btn = tk.Button(lower_frame , text = "Play",height=2, width=40 , command = play_pause)
play_pause_btn.pack(expand = True,fill = "both" , side = LEFT)

Button_frwrd = PhotoImage(file="forward button.png")
backf = tk.Button(lower_frame,image=Button_frwrd , bd=0 , width=50 ,height=50 , command = lambda:skip(5)).pack(side = LEFT)

vid_player.bind("<<Duration>>" , update_duration)
vid_player.bind("<<SecondChanged>>" , update_scale)
vid_player.bind("<<Ended>>" , video_ended)
vid_player1.bind("<<Duration>>" , update_duration)
vid_player1.bind("<<SecondChanged>>" , update_scale)
vid_player1.bind("<<Ended>>" , video_ended)

root.mainloop()