from moviepy.editor import VideoFileClip

input_video = "input_video.mp4"
output_video = "output_video.mp4"

clip = VideoFileClip(input_video)
# Perform operations on the video clip (e.g., resize, edit)
# For example:
resized_clip = clip.resize(width=1280)
resized_clip.write_videofile(output_video, codec="libx264", fps=24)
