#!/bin/bash

# Process emotion sprites: crop to 500×688 from current 600×850
# Centered horizontally, anchoring at top

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

echo "Processing emotion sprites to 500×688..."
for emotion in "${emotions[@]}"; do
    input="$SPRITE_DIR/${emotion}.png"
    if [ -f "$input" ]; then
        # Crop 500 wide × 688 tall, centered horizontally (+50 offset left)
        magick "$input" -crop 500x688+50+0 +repage "$input"
        echo "✓ $emotion.png"
    else
        echo "✗ $emotion.png not found"
    fi
done

echo "Done!"
