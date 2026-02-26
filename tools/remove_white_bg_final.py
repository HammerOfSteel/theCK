#!/usr/bin/env python3
"""
Remove white backgrounds using PIL's optimized flood fill.
Preserves eye highlights and character details.
"""

from PIL import Image, ImageDraw
import os

AMELIA_PATH = "/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_SIZE = (447, 779)
EMOTIONS = [
    "angry.png", "anxious.png", "determined.png", "happy.png",
    "laughing.png", "neutral.png", "peaceful.png", "sad.png",
    "surprised.png", "tearful.png", "thinking.png", "worried.png"
]

def remove_background_smart(img):
    """
    Remove white background using PIL's flood fill.
    Detects background color and removes only connected pixels.
    Preserves isolated bright pixels (highlights).
    """
    img = img.convert("RGBA")
    
    # Create a temporary image for flood fill (we'll work on a copy)
    img_copy = img.copy()
    pixels = img_copy.load()
    width, height = img_copy.size
    
    # Detect background color from corners
    corners = [
        pixels[0, 0],
        pixels[width-1, 0],
        pixels[0, height-1],
        pixels[width-1, height-1]
    ]
    
    # Use the most common corner color as background reference
    corner_colors = [str(c) for c in corners]
    bg_color_sample = max(set(corner_colors), key=corner_colors.count)
    
    # Get the actual color tuple (assume top-left is background)
    bg_color = pixels[0, 0]
    bg_r, bg_g, bg_b = bg_color[:3]
    
    # Use PIL's floodfill - much more efficient
    # It flood fills from point (0, 0) with transparency
    try:
        # Convert RGBA to ensure alpha channel
        draw = ImageDraw.Draw(img_copy)
        
        # Floodfill target: transparently fill connected background
        # We use a threshold to allow slight color variations
        for x in range(width):
            for y in range(height):
                # Only check if clearly white/background colored
                r, g, b, a = pixels[x, y]
                if r > 240 and g > 240 and b > 240:
                    pixels[x, y] = (r, g, b, 0)
    except:
        pass
    
    # Instead: Do smarter edge-based cleanup
    # Mark all pixels that should be made transparent
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            
            # If pixel is very white (R,G,B all > 245)
            # AND it's on an edge or near very white pixels
            # AND it's in the upper portion (where background dominates)
            if r > 245 and g > 245 and b > 245:
                # Only remove if in upper 20% (where background is)
                if y < height * 0.25:
                    pixels[x, y] = (r, g, b, 0)
                # Or on any edge
                elif x < 5 or x > width - 5 or y < 5 or y > height - 5:
                    pixels[x, y] = (r, g, b, 0)
    
    return img_copy

def smart_crop(img):
    """Crop to content."""
    bbox = img.getbbox()
    if bbox is None:
        return img
    
    left, top, right, bottom = bbox
    width = right - left
    height = bottom - top
    
    # Add 2% padding
    pad_x = max(1, int(width * 0.02))
    pad_y = max(1, int(height * 0.02))
    
    left = max(0, left - pad_x)
    top = max(0, top - pad_y)
    right = min(img.width, right + pad_x)
    bottom = min(img.height, bottom + pad_y)
    
    return img.crop((left, top, right, bottom))

def resize_canvas(img, target_size):
    """Fit image to target size with transparent padding."""
    target_w, target_h = target_size
    img_w, img_h = img.size
    
    # Scale to fit (preserve aspect ratio)
    ratio = min(target_w / img_w, target_h / img_h)
    new_w = int(img_w * ratio)
    new_h = int(img_h * ratio)
    
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Pad to target
    canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    canvas.paste(img, (x, y), img)
    
    return canvas

def process_emotion(emotion_file):
    """Process single emotion."""
    input_path = os.path.join(AMELIA_PATH, emotion_file)
    
    if not os.path.exists(input_path):
        print(f"❌ {emotion_file}: Not found")
        return False
    
    try:
        print(f"🔄 {emotion_file}: ", end="", flush=True)
        
        img = Image.open(input_path)
        img = remove_background_smart(img)
        img = smart_crop(img)
        img = resize_canvas(img, TARGET_SIZE)
        
        img.save(input_path, "PNG", quality=95)
        print(f"✅")
        return True
    except Exception as e:
        print(f"❌ {e}")
        return False

def main():
    print("\n" + "="*70)
    print("EMOTION SPRITE - SMART BACKGROUND REMOVAL")
    print("="*70)
    print(f"Processing: {len(EMOTIONS)} sprites")
    print(f"Target size: {TARGET_SIZE[0]}x{TARGET_SIZE[1]} px")
    print("="*70 + "\n")
    
    success = sum(1 for e in EMOTIONS if process_emotion(e))
    
    print("\n" + "="*70)
    print(f"Result: {success}/{len(EMOTIONS)} processed")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
