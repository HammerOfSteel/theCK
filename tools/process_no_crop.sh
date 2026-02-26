#!/bin/bash
# NO CROPPING - Just make white transparent and fit to canvas with padding

AMELIA_PATH="/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_SIZE="447x779"

EMOTIONS=(
    "angry.png" "anxious.png" "determined.png" "happy.png"
    "laughing.png" "neutral.png" "peaceful.png" "sad.png"
    "surprised.png" "tearful.png" "thinking.png" "worried.png"
)

echo "Processing (NO CROPPING - transparent white, preserve full character)..."
echo ""

for emotion in "${EMOTIONS[@]}"; do
    input="$AMELIA_PATH/$emotion"
    [ ! -f "$input" ] && { echo "❌ $emotion"; continue; }
    
    echo -n "$emotion: "
    
    # ONLY:
    # 1. Make white transparent
    # 2. Fit to 447x779 without trimming, just add padding
    magick "$input" \
        -fuzz 0% \
        -transparent white \
        -background none \
        -gravity Center \
        -extent "$TARGET_SIZE" \
        "$input" 2>/dev/null && echo "✅" || echo "❌"
done

echo ""
echo "Done!"
