from moviepy.editor import VideoFileClip, concatenate_videoclips

video_paths = ["path/to/video1.mp4", "path/to/video2.mp4", "path/to/video3.mp4"]

video_clips = [VideoFileClip(path) for path in video_paths]

final_clip = concatenate_videoclips(video_clips)

final_clip.write_videofile("path/to/concatenated_video.mp4")
