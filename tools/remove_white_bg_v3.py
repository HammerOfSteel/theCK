#!/usr/bin/env python3
"""
Remove white backgrounds from emotion sprites using flood-fill.
Preserves eye highlights and character details by only removing 
connected background pixels from the edges.
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

def flood_fill_background(img):
    """
    Use flood fill to remove only the background.
    This preserves isolated white pixels (like eye highlights).
    """
    img = img.convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    # Detect the background color from corners (assume corners are background)
    corners = [
        pixels[0, 0],           # Top-left
        pixels[width-1, 0],     # Top-right
        pixels[0, height-1],    # Bottom-left
        pixels[width-1, height-1]  # Bottom-right
    ]
    
    # Most common corner color is the background
    bg_color = max(set(corners), key=corners.count)
    bg_r, bg_g, bg_b = bg_color[:3]
    
    # Allow some tolerance for variations
    tolerance = 30
    
    def is_background(pixel):
        """Check if pixel color matches background."""
        r, g, b, a = pixel
        return (abs(r - bg_r) < tolerance and 
                abs(g - bg_g) < tolerance and 
                abs(b - bg_b) < tolerance)
    
    # Flood fill from edges - mark pixels to remove
    to_remove = set()
    
    def flood_fill(x, y):
        """Recursively mark connected background pixels."""
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        if (x, y) in to_remove:
            return
        
        pixel = pixels[x, y]
        if not is_background(pixel):
            return
        
        to_remove.add((x, y))
        
        # Fill neighbors
        flood_fill(x+1, y)
        flood_fill(x-1, y)
        flood_fill(x, y+1)
        flood_fill(x, y-1)
    
    # Start flood fill from all edges
    for x in range(width):
        flood_fill(x, 0)           # Top edge
        flood_fill(x, height-1)    # Bottom edge
    for y in range(height):
        flood_fill(0, y)           # Left edge
        flood_fill(width-1, y)     # Right edge
    
    # Apply removal
    for x, y in to_remove:
        r, g, b = pixels[x, y][:3]
        pixels[x, y] = (r, g, b, 0)
    
    return img

def smart_crop(img):
    """Crop to content, preserving character details."""
    bbox = img.getbbox()
    if bbox is None:
        return img
    
    left, top, right, bottom = bbox
    
    # Minimal padding - just 1% to not cut edges
    width = right - left
    height = bottom - top
    padding_x = max(1, int(width * 0.01))
    padding_y = max(1, int(height * 0.01))
    
    left = max(0, left - padding_x)
    top = max(0, top - padding_y)
    right = min(img.width, right + padding_x)
    bottom = min(img.height, bottom + padding_y)
    
    return img.crop((left, top, right, bottom))

def resize_to_target(img, target_size):
    """Resize to target while maintaining aspect ratio and filling space."""
    target_w, target_h = target_size
    img_w, img_h = img.size
    
    # Calculate scale to fill target (don't shrink below target)
    scale_w = target_w / img_w
    scale_h = target_h / img_h
    scale = max(scale_w, scale_h)
    
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    
    # Resize with high quality
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Create target canvas
    canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
    
    # Center
    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    canvas.paste(img, (x, y), img)
    
    return canvas

def process_emotion(emotion_file):
    """Process single emotion sprite."""
    input_path = os.path.join(AMELIA_PATH, emotion_file)
    
    if not os.path.exists(input_path):
        print(f"❌ {emotion_file}: Not found")
        return False
    
    try:
        print(f"🔄 {emotion_file}: ", end="", flush=True)
        
        img = Image.open(input_path)
        img = flood_fill_background(img)
        img = smart_crop(img)
        img = resize_to_target(img, TARGET_SIZE)
        
        img.save(input_path, "PNG", quality=95)
        print(f"✅")
        return True
    except Exception as e:
        print(f"❌ {e}")
        return False

def main():
    print("\n" + "="*70)
    print("EMOTION SPRITE - FLOOD FILL BACKGROUND REMOVAL")
    print("="*70)
    print(f"Processing: {len(EMOTIONS)} sprites")
    print(f"Method: Flood-fill from edges (preserves highlights)")
    print(f"Target size: {TARGET_SIZE[0]}x{TARGET_SIZE[1]} px")
    print("="*70 + "\n")
    
    if not os.path.exists(AMELIA_PATH):
        print(f"❌ Path not found: {AMELIA_PATH}\n")
        return
    
    success = sum(1 for emotion in EMOTIONS if process_emotion(emotion))
    
    print("\n" + "="*70)
    print(f"Result: {success}/{len(EMOTIONS)} processed")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
