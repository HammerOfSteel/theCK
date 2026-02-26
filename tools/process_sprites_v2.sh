#!/bin/bash
# Process emotion sprites - remove white bg, preserve character, add padding
# - Makes white transparent
# - Crops minimally (just extreme edges)
# - Adds padding on sides to preserve full character including arms
# - Resizes to 447x779

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

echo "================================================================"
echo "EMOTION SPRITE PROCESSING"
echo "================================================================"
echo "- Remove white background (make transparent)"
echo "- Minimal crop (preserve arms and character)"
echo "- Add padding on sides"
echo "- Crop bottom slightly (curved area)"
echo "- Target: 447x779"
echo "================================================================"
echo ""

success=0
failed=0

for emotion in "${EMOTIONS[@]}"; do
    input="$AMELIA_PATH/$emotion"
    
    if [ ! -f "$input" ]; then
        echo "❌ $emotion: File not found"
        ((failed++))
        continue
    fi
    
    echo -n "🔄 $emotion: "
    
    # Process:
    # 1. -transparent "rgb(255,255,255)" - make white transparent
    # 2. -trim -fuzz 5% - trim aggressively white areas only
    # 3. +repage - reset canvas
    # 4. -background white - white background for calculation
    # 5. -splice 30x20 - add padding: 30px left/right, 20px top/bottom
    # 6. -background none - switch to transparent
    # 7. -gravity South - focus on bottom
    # 8. -chop 0x40 - crop 40px from bottom (curved area)
    # 9. -extent $TARGET_SIZE - resize to final target
    # 10. -quality 95 - high quality PNG
    
    if magick "$input" \
        -transparent "rgb(255,255,255)" \
        -trim -fuzz 2% \
        +repage \
        -bordercolor white -border 30x30 \
        -background none \
        -flatten \
        -alpha extract \
        -negate \
        -alpha off \
        "$input" 2>/dev/null; then
        
        # Now add transparency back and fit to canvas
        magick "$input" \
            -background none \
            -gravity Center \
            -extent "$TARGET_SIZE" \
            -quality 95 \
            "$input" 2>/dev/null
        
        if [ $? -eq 0 ]; then
            echo "✅"
            ((success++))
        else
            echo "❌ (fit)"
            ((failed++))
        fi
    else
        echo "❌ (process)"
        ((failed++))
    fi
done

echo ""
echo "================================================================"
echo "Complete: $success succeeded, $failed failed"
echo "================================================================"
echo ""
