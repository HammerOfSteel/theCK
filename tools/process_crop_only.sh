#!/bin/bash
# Process sprites correctly:
# 1. Make white transparent (not resize)
# 2. Crop to remove white space
# 3. Fit to 447x779 canvas with character at full size
# 4. Put padding on sides (crop minimal from sides, more from bottom)

AMELIA_PATH="/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_WIDTH=447
TARGET_HEIGHT=779

EMOTIONS=(
    "angry.png" "anxious.png" "determined.png" "happy.png"
    "laughing.png" "neutral.png" "peaceful.png" "sad.png"
    "surprised.png" "tearful.png" "thinking.png" "worried.png"
)

echo "Processing sprites..."
echo "- Make white transparent"
echo "- Minimal crop (keep character full size)"
echo "- Fit to 447x779 with side padding"
echo ""

for emotion in "${EMOTIONS[@]}"; do
    input="$AMELIA_PATH/$emotion"
    [ ! -f "$input" ] && { echo "❌ $emotion not found"; continue; }
    
    echo -n "$emotion: "
    
    # Process:
    # 1. Make white/near-white transparent (fuzz 2%)
    # 2. No resize of character - just make canvas fit
    # 3. -extent: fit to canvas, centered
    # This keeps character at original size, just adds/removes padding on canvas
    
    if magick "$input" \
        -fuzz 2% \
        -transparent white \
        -background none \
        -gravity Center \
        -extent "${TARGET_WIDTH}x${TARGET_HEIGHT}" \
        "$input" 2>/dev/null; then
        echo "✅"
    else
        echo "❌"
    fi
done

echo ""
echo "Done!"
