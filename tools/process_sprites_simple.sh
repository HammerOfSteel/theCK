#!/bin/bash
# Process emotion sprites - simple approach
# Make white transparent, preserve full character, pad to 447x779

AMELIA_PATH="/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_SIZE="447x779"

EMOTIONS=(
    "angry.png" "anxious.png" "determined.png" "happy.png"
    "laughing.png" "neutral.png" "peaceful.png" "sad.png"
    "surprised.png" "tearful.png" "thinking.png" "worried.png"
)

echo "================================================================"
echo "SPRITE PROCESSING - Remove white bg, add side padding"
echo "================================================================"
echo ""

success=0
for emotion in "${EMOTIONS[@]}"; do
    input="$AMELIA_PATH/$emotion"
    [ ! -f "$input" ] && { echo "❌ $emotion: Not found"; ((failed++)); continue; }
    
    echo -n "🔄 $emotion: "
    
    # Simple approach:
    # 1. Make white transparent
    # 2. Add white border padding (30px sides, 10px top, 50px bottom for crop)
    # 3. Make border transparent
    # 4. Fit exactly to 447x779
    
    if magick "$input" \
        -transparent white \
        -bordercolor white -border 30x10 \
        -background none \
        -alpha on \
        -virtual-pixel none \
        -bordercolor none -border 0x40 \
        -gravity Center \
        -extent "$TARGET_SIZE" \
        -quality 95 \
        "$input" 2>/dev/null; then
        echo "✅"
        ((success++))
    else
        echo "❌"
        ((failed++))
    fi
done

echo ""
echo "================================================================"
echo "Result: $success/12 processed"
echo "================================================================"
