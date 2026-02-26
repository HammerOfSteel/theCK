#!/bin/bash
# Remove white backgrounds and crop sprites using ImageMagick
# - Removes pure white background
# - Crops to fit character (crops bottom curve slightly)
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
echo "EMOTION SPRITE PROCESSING (ImageMagick)"
echo "================================================================"
echo "Removing white backgrounds + cropping to character"
echo "Target size: $TARGET_SIZE"
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
    
    # Process with ImageMagick:
    # 1. -transparent "rgb(255,255,255)" - make white transparent
    # 2. -trim - remove white borders
    # 3. +repage - reset virtual canvas
    # 4. -background none - transparent background
    # 5. -gravity Center - center alignment
    # 6. -extent $TARGET_SIZE - fit to target size (centered, transparent padding)
    # 7. -quality 95 - high quality PNG
    
    if magick "$input" \
        -transparent "rgb(255,255,255)" \
        -trim \
        +repage \
        -background none \
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
echo "Complete: $success succeeded, $failed failed"
echo "================================================================"
echo ""
