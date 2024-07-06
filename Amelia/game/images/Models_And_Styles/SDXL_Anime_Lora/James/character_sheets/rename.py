import os
import glob

def rename_images():
    # Define the base path where the images are located (current directory)
    path = os.getcwd()
    
    # List all PNG files, sorted by creation time (oldest first)
    files = sorted(glob.glob(os.path.join(path, '*.png')), key=os.path.getctime)
    
    # Define emotions and the number of clothing sets

    emotions = ["happy", "sad", "angry", "surprised", "scared", "confused", "excited", "worried",
                 "indifferent", "nervous", "determined", "relieved", "skeptical", "embarrassed", 
                 "curious", "tired", "hopeful", "jealous", "loving", "thankful", "depressed", 
                 "crying", "serene", "neutral", "disgusted"]
    cloth_sets = 5
    images_per_set = 5
    i = 0
    
    # Check if the number of files matches the expected count
    expected_count = len(emotions) * cloth_sets * images_per_set
    if len(files) != expected_count:
        print("Warning: The number of files in the directory does not match the expected number.")
    
    # Rename files according to the specified format
    file_index = 0
    for emotion in emotions:
        for set_number in range(1, cloth_sets + 1):
            i = i + 1
            if set_number == 1 and emotion == "angry":
                images_per_set = 4
            else:
                images_per_set = 5
            for image_number in range(1, images_per_set + 1):
                old_file = files[file_index]
                new_file = f"james_{emotion}_sheet_cloths{set_number}"
                if image_number > 1:
                    new_file += f"_{image_number}"
                new_file += ".png"
                os.rename(old_file, os.path.join(path, new_file))
                print(f"Renamed '{old_file}' to '{new_file}'")
                file_index += 1

if __name__ == "__main__":
    rename_images()