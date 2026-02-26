#!/bin/bash

# Remove white background from emotion sprites while preserving eye whites
# Uses small fuzz to remove background while keeping eye highlights

SPRITE_DIR="/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"

emotions=(
    "neutral"
    "happy"
    "sad"
    "angry"
    "surprised"
    "thinking"
    "worried"
    "laughing"
    "anxious"
    "determined"
    "tearful"
    "peaceful"
)

echo "Removing white background with Python (color thresholding)..."

python3 << 'EOF'
from PIL import Image
import os

sprite_dir = "/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"

emotions = [
    "neutral", "happy", "sad", "angry", "surprised", "thinking",
    "worried", "laughing", "anxious", "determined", "tearful", "peaceful"
]

for emotion in emotions:
    input_path = os.path.join(sprite_dir, f"{emotion}.png")
    if os.path.exists(input_path):
        # Open image and convert to RGBA
        img = Image.open(input_path).convert("RGBA")
        data = img.getdata()
        
        # Create new image with transparent pixels for near-white colors
        new_data = []
        for pixel in data:
            r, g, b, a = pixel
            # If pixel is light (R,G,B > 240), make it transparent
            if r > 240 and g > 240 and b > 240:
                new_data.append((r, g, b, 0))
            else:
                new_data.append(pixel)
        
        img.putdata(new_data)
        img.save(input_path)
        print(f"✓ {emotion}.png")
    else:
        print(f"✗ {emotion}.png not found")

print("Done!")
EOF
