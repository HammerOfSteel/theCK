import os
import glob

# Define the emotional categories and the base name for the files
emotions = [
    "happy", "sad", "angry", "surprised", "scared", "disgusted", "confused",
    "excited", "worried", "indifferent", "nervous", "determined", "relieved",
    "skeptical", "embarrassed", "curious", "tired", "hopeful", "jealous",
    "loving", "thankful", "depressed", "crying", "serene", "neutral"
]

base_name = "fullbody_amelia_"

# Get all png files in the directory, sorted by creation time (oldest first)
files = sorted(glob.glob('*.png'), key=os.path.getmtime)

# Function to rename files
def rename_files(files, emotions, base_name):
    index = 0
    for emotion in emotions:
        for i in range(5):
            old_name = files[index]
            new_name = f"{base_name}{emotion}{'' if i == 0 else '_' + str(i + 1)}.png"
            os.rename(old_name, new_name)
            index += 1

# Call the rename function
rename_files(files, emotions, base_name)
