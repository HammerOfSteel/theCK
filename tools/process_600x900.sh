#!/bin/bash
# Process to 600x900 - preserves character width, keeps full height

AMELIA_PATH="/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_SIZE="600x900"

EMOTIONS=(
    "angry.png" "anxious.png" "determined.png" "happy.png"
    "laughing.png" "neutral.png" "peaceful.png" "sad.png"
    "surprised.png" "tearful.png" "thinking.png" "worried.png"
)

echo "Processing to 600x900..."
echo ""

for emotion in "${EMOTIONS[@]}"; do
    input="$AMELIA_PATH/$emotion"
    [ ! -f "$input" ] && { echo "❌ $emotion"; continue; }
    
    echo -n "$emotion: "
    
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
