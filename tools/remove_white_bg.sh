#!/bin/bash
# Remove white backgrounds from emotion sprites using ImageMagick
# This preserves character quality and properly crops/resizes

AMELIA_PATH="/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/images/characters/amelia"
TARGET_SIZE="447x779"

EMOTIONS=(
    "angry.png"
    "anxious.png"
    "determined.png"
    "happy.png"
    "laughing.png"
    "neutral.png"
    "peaceful.png"
    "sad.png"
    "surprised.png"
    "tearful.png"
    "thinking.png"
    "worried.png"
)

echo "============================================================"
echo "EMOTION SPRITE BACKGROUND REMOVAL (ImageMagick)"
echo "============================================================"
echo "Source: $AMELIA_PATH"
echo "Target size: $TARGET_SIZE"
echo "============================================================"
echo ""

success=0
failed=0

for emotion in "${EMOTIONS[@]}"; do
    input="$AMELIA_PATH/$emotion"
    temp="$AMELIA_PATH/${emotion%.png}_temp.png"
    
    if [ ! -f "$input" ]; then
        echo "❌ $emotion: File not found"
        ((failed++))
        continue
    fi
    
    echo -n "🔄 $emotion: Processing... "
    
    # Use ImageMagick to:
    # 1. -background white: Set background to white (for flatten prep)
    # 2. -transparent "rgb(255,255,255)": Make white transparent
    # 3. -trim: Remove white borders
    # 4. +repage: Remove virtual canvas offset
    # 5. -background none: Transparent background
    # 6. -gravity Center: Center alignment
    # 7. -extent $TARGET_SIZE: Resize to target, centered
    # 8. -quality 95: High quality PNG
    
    if convert "$input" \
        -transparent "rgb(255,255,255)" \
        -trim \
        +repage \
        -background none \
        -gravity Center \
        -extent "$TARGET_SIZE" \
        -quality 95 \
        "$temp" 2>/dev/null; then
        
        # Move temp to final location
        mv "$temp" "$input"
        echo "✅"
        ((success++))
    else
        echo "❌ Error"
        rm -f "$temp"
        ((failed++))
    fi
done

echo ""
echo "============================================================"
echo "Complete: $success succeeded, $failed failed"
echo "============================================================"
echo ""
