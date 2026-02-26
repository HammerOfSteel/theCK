#!/usr/bin/env python3
"""
Remove white backgrounds from emotion PNG sprites - improved version.
Preserves character quality while removing backgrounds.
"""

from PIL import Image
import os

AMELIA_PATH = "/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_SIZE = (447, 779)
EMOTIONS = [
    "angry.png", "anxious.png", "determined.png", "happy.png",
    "laughing.png", "neutral.png", "peaceful.png", "sad.png",
    "surprised.png", "tearful.png", "thinking.png", "worried.png"
]

def remove_white_background(img):
    """Remove white/near-white background. Keep actual character colors."""
    img = img.convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    # Make near-white pixels transparent (but preserve actual colors)
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # If the pixel is very light (close to white) and desaturated
            # Mark it as potentially background
            luminance = (r + g + b) / 3
            max_channel = max(r, g, b)
            min_channel = min(r, g, b)
            saturation = (max_channel - min_channel) / max_channel if max_channel > 0 else 0
            
            # Remove if: very bright AND desaturated (nearly white)
            if luminance > 235 and saturation < 0.1:
                pixels[x, y] = (r, g, b, 0)
    
    return img

def smart_crop(img):
    """Crop to content, finding actual character bounds."""
    bbox = img.getbbox()
    if bbox is None:
        return img
    
    left, top, right, bottom = bbox
    
    # Add small padding to not cut off edges (5%)
    width = right - left
    height = bottom - top
    left = max(0, left - int(width * 0.02))
    top = max(0, top - int(height * 0.02))
    right = min(img.width, right + int(width * 0.02))
    bottom = min(img.height, bottom + int(height * 0.02))
    
    return img.crop((left, top, right, bottom))

def resize_to_fill(img, target_size):
    """Resize to fill target size while maintaining aspect ratio."""
    target_w, target_h = target_size
    
    # Calculate scaling to fill target (don't shrink)
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h
    
    if img_ratio > target_ratio:
        # Image is wider, scale by height
        new_h = target_h
        new_w = int(new_h * img_ratio)
    else:
        # Image is taller, scale by width
        new_w = target_w
        new_h = int(new_w / img_ratio)
    
    # Resize with high-quality resampling
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Create target canvas with transparent background
    canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
    
    # Center image on canvas
    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    canvas.paste(img, (x, y), img)
    
    return canvas

def process_emotion(emotion_file):
    """Process single emotion sprite."""
    input_path = os.path.join(AMELIA_PATH, emotion_file)
    
    if not os.path.exists(input_path):
        print(f"❌ {emotion_file}: File not found")
        return False
    
    try:
        print(f"🔄 {emotion_file}: ", end="", flush=True)
        
        # Load and process
        img = Image.open(input_path)
        img = remove_white_background(img)
        img = smart_crop(img)
        img = resize_to_fill(img, TARGET_SIZE)
        
        # Save
        img.save(input_path, "PNG", quality=95)
        print(f"✅")
        return True
    except Exception as e:
        print(f"❌ {e}")
        return False

def main():
    print("\n" + "="*70)
    print("EMOTION SPRITE BACKGROUND REMOVAL (Improved)")
    print("="*70)
    print(f"Processing: {len(EMOTIONS)} sprites")
    print(f"Target size: {TARGET_SIZE[0]}x{TARGET_SIZE[1]} px")
    print("="*70 + "\n")
    
    if not os.path.exists(AMELIA_PATH):
        print(f"❌ Path not found: {AMELIA_PATH}\n")
        return
    
    success = sum(1 for emotion in EMOTIONS if process_emotion(emotion))
    
    print("\n" + "="*70)
    print(f"Result: {success}/{len(EMOTIONS)} processed successfully")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
