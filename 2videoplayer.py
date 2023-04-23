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

vid_player1: TkinterVideo = TkinterVideo(root, scaled = True)
vid_player1.pack(side=LEFT, expand = True, fill = "both")

vid_player2: TkinterVideo = TkinterVideo(root, scaled = True)
vid_player2.pack(side=LEFT, expand = True, fill = "both")

def update_duration(event):
     duration = vid_player1.video_info()["duration"]

     end_time1["text"] = str(datetime.timedelta(seconds = duration))
     progress_slider1["to"] = duration

     duration = vid_player2.video_info()["duration"]

     end_time2["text"] = str(datetime.timedelta(seconds = duration))
     progress_slider2["to"] = duration

def update_scale(event):
    progress_value1.set(vid_player1.current_duration())
    progress_value2.set(vid_player2.current_duration())


def load_video1():
    file_path = filedialog.askopenfilename()
    if file_path:
        vid_player1.load(file_path)
        progress_slider1.config(to=0, from_=0)
        play_pause_btn1["text"] = "play"
        progress_value1.set(0)


def load_video2():
    file_path = filedialog.askopenfilename()
    if file_path:
        vid_player2.load(file_path)
        progress_slider2.config(to=0, from_=0)
        play_pause_btn2["text"] = "play"
        progress_value2.set(0)


load_btn1 = tk.Button(lower_frame, text="Load Video 1", command=load_video1)
load_btn1.pack(side=LEFT)

load_btn2 = tk.Button(lower_frame, text="Load Video 2", command=load_video2)
load_btn2.pack(side=LEFT)


def seek1(value):
    vid_player1.seek(int(value))

def seek2(value):
    vid_player2.seek(int(value))

def skip1(value:int):
    vid_player1.seek(int(progress_slider1.get())+value)
    progress_value1.set(progress_slider1.get()+value)

def skip2(value:int):
    vid_player2.seek(int(progress_slider2.get())+value)
    progress_value2.set(progress_slider2.get()+value)

def play_pause1():
    if vid_player1.is_paused():
        vid_player1.play()
        play_pause_btn1["text"] = "Pause"

    else:
        vid_player1.pause()
        play_pause_btn1["text"] = "play"

def play_pause2():
    if vid_player2.is_paused():
        vid_player2.play()
        play_pause_btn2["text"] = "Pause"

    else:
        vid_player2.pause()
        play_pause_btn2["text"] = "play"


def video_ended1(event):
    progress_slider1.set(progress_slider1["to"])
    play_pause_btn1["text"] = "Play"
    progress_slider1.set(0)

def video_ended2(event):
    progress_slider2.set(progress_slider2["to"])
    play_pause_btn2["text"] = "Play"
    progress_slider2.set(0)


start_time1 = tk
start_time1 = tk.Label(lower_frame, text="00:00:00", font=("Helvetica", 10))
start_time1.pack(side=LEFT)

progress_slider1 = tk.Scale(lower_frame, orient = HORIZONTAL, command = seek1)
progress_slider1.pack(side=LEFT, fill = "both", expand = True)

end_time1 = tk.Label(lower_frame, text="00:00:00", font=("Helvetica", 10))
end_time1.pack(side=LEFT)

skip_back_btn1 = tk.Button(lower_frame, text="<<10s", command=lambda: skip1(-10))
skip_back_btn1.pack(side=LEFT)

play_pause_btn1 = tk.Button(lower_frame, text="Play", command=play_pause1)
play_pause_btn1.pack(side=LEFT)

skip_forward_btn1 = tk.Button(lower_frame, text="10s>>", command=lambda: skip1(10))
skip_forward_btn1.pack(side=LEFT)

progress_value1 = tk.DoubleVar()
vid_player1.bind("<<VideoPositionChanged>>", update_scale)
vid_player1.bind("<<VideoLoaded>>", update_duration)
vid_player1.bind("<<VideoEnded>>", video_ended1)

start_time2 = tk.Label(lower_frame, text="00:00:00", font=("Helvetica", 10))
start_time2.pack(side=LEFT)

progress_slider2 = tk.Scale(lower_frame, orient = HORIZONTAL, command = seek2)
progress_slider2.pack(side=LEFT, fill = "both", expand = True)

end_time2 = tk.Label(lower_frame, text="00:00:00", font=("Helvetica", 10))
end_time2.pack(side=LEFT)

skip_back_btn2 = tk.Button(lower_frame, text="<<10s", command=lambda: skip2(-10))
skip_back_btn2.pack(side=LEFT)

play_pause_btn2 = tk.Button(lower_frame, text="Play", command=play_pause2)
play_pause_btn2.pack(side=LEFT)

skip_forward_btn2 = tk.Button(lower_frame, text="10s>>", command=lambda: skip2(10))
skip_forward_btn2.pack(side=LEFT)

progress_value2 = tk.DoubleVar()
vid_player2.bind("<<VideoPositionChanged>>", update_scale)
vid_player2.bind("<<VideoLoaded>>", update_duration)
vid_player2.bind("<<VideoEnded>>", video_ended2)

root.mainloop()