import os
import glob

def rename_images():
    # Define the base path where the images are located (current directory)
    path = os.getcwd()
    
    # List all PNG files, sorted by creation time (oldest first)
    files = sorted(glob.glob(os.path.join(path, '*.png')), key=os.path.getctime)
    
    # Define emotions and the number of clothing sets
    emotions = ["sad", "happy", "angry", "surprised", "scared", "confused", "excited", "worried",
                 "indifferent", "nervous", "determined", "relieved", "skeptical", "embarrassed", 
                 "curious", "tired", "hopeful", "jealous", "loving", "thankful", "depressed", 
                 "crying", "serene", "neutral"]
    cloth_sets = 5
    images_per_set = 5
    
    # Check if the number of files matches the expected count
    expected_count = len(emotions) * cloth_sets * images_per_set
    if len(files) != expected_count:
        print("Warning: The number of files in the directory does not match the expected number.")
    
    # Rename files according to the specified format
    file_index = 0
    for emotion in emotions:
        for set_number in range(1, cloth_sets + 1):
            if emotion == "crying" and set_number == 1:
                images_per_set = 4
            if emotion == "curious" and set_number == 1:
                images_per_set = 4
            if emotion == "determined" and set_number == 1:
                images_per_set = 4
            if emotion == "excited" and set_number == 2:
                images_per_set = 4
            if emotion == "neutral" and set_number == 5:
                images_per_set = 4
            if emotion == "thankful" and set_number == 1:
                images_per_set = 4
            if emotion == "tired" and set_number == 1:
                images_per_set = 4
            if emotion == "worried" and set_number == 1:
                images_per_set = 4
            # if emotion == "happy" and set_number == 1:
            #     images_per_set = 6
            # if emotion == "sad" and set_number == 1:
            #     images_per_set = 6
            # if emotion == "surprised" and set_number == 1:
            #     images_per_set = 6
            else:
                images_per_set = 5
            for image_number in range(1, images_per_set + 1):
                old_file = files[file_index]
                new_file = f"1_mom_{emotion}_sheet_cloths{set_number}"
                if image_number > 1:
                    new_file += f"_{image_number}"
                new_file += ".png"
                os.rename(old_file, os.path.join(path, new_file))
                print(f"Renamed '{old_file}' to '{new_file}'")
                file_index += 1

if __name__ == "__main__":
    rename_images()