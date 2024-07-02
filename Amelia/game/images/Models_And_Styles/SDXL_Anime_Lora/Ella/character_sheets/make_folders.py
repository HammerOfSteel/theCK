import os

# List of main folders
main_folders = [
    'sad', 'angry', 'surprised', 'scared', 'disgusted', 'confused',
    'excited', 'worried', 'indifferent', 'nervous', 'determined', 'relieved',
    'skeptical', 'embarrased', 'curious', 'tired', 'hopeful', 'jealous',
    'loving', 'thankful', 'depressed', 'crying', 'serene', 'neutral'
]

# List of subfolders
sub_folders = ['cloths_1', 'cloths_2', 'cloths_3', 'cloths_4', 'cloths_5']

# Create main folders and subfolders
for main_folder in main_folders:
    # Create main folder
    os.makedirs(main_folder, exist_ok=True)
    
    # Create subfolders within each main folder
    for sub_folder in sub_folders:
        os.makedirs(os.path.join(main_folder, sub_folder), exist_ok=True)

print("Folders created successfully.")