import pafy
from moviepy.video.io.VideoFileClip import VideoFileClip

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

video = pafy.new(video_url)
best = video.getbest(preftype="mp4")
best.download()

title = video.title
title = title.replace(" ","_")

video = VideoFileClip(best.filename)

start_time = 0
end_time = video.duration/2

cutout = video.subclip(start_time, end_time)
cutout.write_videofile(f"{title}.mp4", codec='libx264', bitrate="5000k", threads=4, audio_codec='aac', audio_bitrate='256k', preset='ultrafast')
