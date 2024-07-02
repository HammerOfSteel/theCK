import os
import glob
import time

# List of emotions
emotions = [
    "Joyful", "Anxious", "Serene", "Frustrated", "Curious", "Shy", "Confident", "Bored", 
    "Skeptical", "Amused", "Worried", "Determined", "Playful", "Nostalgic", "Angry", "Sad", 
    "Excited", "Tired", "Inspired", "Mocking", "Grateful", "Envious", "Startled", "Proud", 
    "Flirtatious", "Mischievous", "Hopeful", "Disgusted", "Contemplative", "Grieving", "Joyous", 
    "Stressed", "Intrigued", "Horrified", "Relieved", "Sly", "Disappointed", "Indifferent", 
    "Impatient", "Affectionate", "Bewildered", "Vengeful", "Giddy", "Overwhelmed", "Calm", 
    "Sarcastic", "Regretful", "Optimistic", "Sincere", "Jubilant"
]

# Get the current folder name
folder_name = os.path.basename(os.getcwd())

# Get all .png files in the current folder
png_files = glob.glob("*.png")

# Sort the files by creation date (oldest to newest)
png_files.sort(key=os.path.getctime)

# Rename files with emotions
for i, file in enumerate(png_files):
    if i >= len(emotions):
        break
    new_name = f"{folder_name}_{emotions[i]}.png"
    os.rename(file, new_name)

print("Files renamed successfully.")
