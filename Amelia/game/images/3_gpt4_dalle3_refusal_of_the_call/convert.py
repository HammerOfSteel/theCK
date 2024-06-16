import os
from PIL import Image

def convert_webp_to_jpg(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            webp_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename.replace(".webp", ".jpg"))

            # Open the webp image
            with Image.open(webp_path) as img:
                # Convert and save as jpg
                img.convert("RGB").save(jpg_path, "JPEG")

            print(f"Converted {webp_path} to {jpg_path}")

if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    convert_webp_to_jpg(script_dir)
