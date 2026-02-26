#!/bin/bash
# Most basic approach: transparent white, fit to size with padding

AMELIA_PATH="/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_SIZE="447x779"

EMOTIONS=(
    "angry.png" "anxious.png" "determined.png" "happy.png"
    "laughing.png" "neutral.png" "peaceful.png" "sad.png"
    "surprised.png" "tearful.png" "thinking.png" "worried.png"
)

echo "Processing sprites..."
echo ""

for emotion in "${EMOTIONS[@]}"; do
    input="$AMELIA_PATH/$emotion"
    [ ! -f "$input" ] && { echo "❌ $emotion not found"; continue; }
    
    echo -n "$emotion: "
    
    # Step 1: Make white fully transparent
    magick "$input" \
        -fuzz 1% \
        -transparent white \
        -alpha on \
        /tmp/temp_emotion.png 2>/dev/null || { echo "❌"; continue; }
    
    # Step 2: Get image dimensions
    dims=$(magick identify -format "%wx%h" /tmp/temp_emotion.png)
    
    # Step 3: Fit to 447x779 - scale to fit without exceeding either dimension
    # Then center on transparent canvas
    magick /tmp/temp_emotion.png \
        -resize "420x750>" \
        -background none \
        -gravity Center \
        -extent "$TARGET_SIZE" \
        "$input" 2>/dev/null && echo "✅" || echo "❌"
done

rm -f /tmp/temp_emotion.png
echo ""
echo "Done!"
