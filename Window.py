import tkinter as tk
import vlc

class Video_player(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,arent,*args,**kwargs)

        self.instance=vlc.Instance("--no-xlib")

        self.player=self.instance.media_player_new()

        self.video=th.Canvas(self,bg="black")

        self.video.pack(side="top",fill="both",expand=True)

    def open_file(self,fileth):
        

