import cv2
import numpy as np
import os

def process_image(image_path, output_path):
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        return  # skip files that aren't valid images

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold input image as mask
    mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

    # Negate mask
    mask = 255 - mask

    # Apply morphology to remove isolated extraneous noise
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Anti-alias the mask -- blur then stretch
    mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT)
    mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

    # Put mask into alpha channel
    result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask

    # Save resulting masked image
    cv2.imwrite(output_path, result)

# Path where the images are located
directory = '.'

# Loop through all the PNG images in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        output_filename = f"no_bg_{filename}"
        process_image(filename, output_filename)
        print(f"Processed {filename} -> {output_filename}")

print("Background removal completed for all images.")
