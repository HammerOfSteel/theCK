from moviepy.editor import *

# List of your images with the naming format
image_files = ["gui_bg.png"] + [f"gui_bg_{i}.png" for i in range(1, 17)]

# Calculate the duration for each image so that the total video length is 3 minutes
image_duration = 180 / len(image_files)  # 180 seconds = 3 minutes

clips = []
for img_file in image_files:
    # Load image and set its duration
    img_clip = ImageClip(img_file, duration=image_duration)
    
    # Add a fade-in and fade-out transition effect to the image clip
    img_clip = img_clip.crossfadein(1).crossfadeout(1)
    
    clips.append(img_clip)

# Concatenate all clips to create the final video
final_clip = concatenate_videoclips(clips, method="compose")

# Write the result to an MP4 file
final_clip.write_videofile("output_video.mp4", fps=24)
