import os
from PIL import Image

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Loop through all files in the directory
for filename in os.listdir(current_directory):
    # Check if the file is a .webp image
    if filename.endswith('.webp'):
        # Open the .webp image
        with Image.open(os.path.join(current_directory, filename)) as img:
            # Convert the filename to .png
            png_filename = filename.rsplit('.', 1)[0] + '.png'
            # Save the image as .png
            img.save(os.path.join(current_directory, png_filename), 'PNG')

print("Conversion completed!")
