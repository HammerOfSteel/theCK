"""Parser for Ren'Py script files to extract dialogue."""

import re
from pathlib import Path
from typing import List, Dict, Optional


class DialogueLine:
    """Represents a single dialogue line from a .rpy file."""
    
    def __init__(
        self,
        character: str,
        text: str,
        voice_file: Optional[str] = None,
        line_number: int = 0
    ):
        self.character = character
        self.text = text
        self.voice_file = voice_file
        self.line_number = line_number
    
    def __repr__(self):
        return f"DialogueLine({self.character!r}, {self.text[:30]!r}..., voice={self.voice_file})"


class RenpyParser:
    """Parser for Ren'Py .rpy files to extract dialogue."""
    
    # Character name patterns
    CHARACTER_PATTERNS = {
        'a': 'Amelia',
        'ella': 'Ella',
        'hawthorne': 'Prof. Hawthorne',
        'simmons': 'Dr. Simmons',
        'maya': 'Maya',
        'lucas': 'Lucas',
        'zara': 'Zara',
        'raj': 'Raj',
        'sarah': 'Sarah',
        'elena': 'Elena',
        'tasha': 'Tasha',
        'sophia': 'Sophia',
        'liz': 'Liz',
        'michael': 'Michael',
        'david': 'Mr. James',
        'grace': 'Mrs. James',
        'lily': 'Lily',
        'thought': 'Narrator',  # Treat thoughts as narrator
    }
    
    def __init__(self):
        # Pattern for voice lines: voice "audio/narrator/chapter_1/line_001_L38.ogg"
        self.voice_pattern = re.compile(r'voice\s+"([^"]+)"')
        
        # Pattern for character dialogue: ella "Text here"
        self.char_dialogue_pattern = re.compile(r'^(\w+)\s+"(.+)"', re.MULTILINE)
        
        # Pattern for narrator/thought
        self.narrator_pattern = re.compile(r'^"(.+)"$', re.MULTILINE)
        self.thought_pattern = re.compile(r'^thought\s+"(.+)"$', re.MULTILINE)
    
    def parse_file(self, rpy_path: Path) -> List[DialogueLine]:
        """Parse a .rpy file and extract all dialogue lines.
        
        Args:
            rpy_path: Path to the .rpy file
            
        Returns:
            List of DialogueLine objects
        """
        with open(rpy_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        dialogue_lines = []
        current_voice_file = None
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Check for voice directive
            voice_match = self.voice_pattern.search(line)
            if voice_match:
                current_voice_file = voice_match.group(1)
                continue
            
            # Check for thought (treated as narrator)
            thought_match = self.thought_pattern.match(line)
            if thought_match:
                text = thought_match.group(1)
                dialogue_lines.append(DialogueLine(
                    character='Narrator',
                    text=text,
                    voice_file=current_voice_file,
                    line_number=line_num
                ))
                current_voice_file = None
                continue
            
            # Check for character dialogue
            char_match = self.char_dialogue_pattern.match(line)
            if char_match:
                char_code = char_match.group(1).lower()
                text = char_match.group(2)
                
                # Map character code to full name
                character = self.CHARACTER_PATTERNS.get(char_code, char_code.capitalize())
                
                dialogue_lines.append(DialogueLine(
                    character=character,
                    text=text,
                    voice_file=current_voice_file,
                    line_number=line_num
                ))
                current_voice_file = None
                continue
            
            # Check for narrator (plain quoted text)
            narrator_match = self.narrator_pattern.match(line)
            if narrator_match:
                text = narrator_match.group(1)
                # Skip if it's likely a scene directive or menu option
                if not any(keyword in text.lower() for keyword in ['menu:', 'scene', 'with', 'play', 'stop']):
                    dialogue_lines.append(DialogueLine(
                        character='Narrator',
                        text=text,
                        voice_file=current_voice_file,
                        line_number=line_num
                    ))
                    current_voice_file = None
        
        return dialogue_lines
    
    def get_chapter_files(self, game_dir: Path) -> Dict[str, Path]:
        """Get all chapter .rpy files from the game directory.
        
        Args:
            game_dir: Path to the game directory
            
        Returns:
            Dictionary mapping chapter names to file paths
        """
        chapter_files = {}
        
        for rpy_file in game_dir.glob("chapter_*.rpy"):
            chapter_name = rpy_file.stem  # e.g., "chapter_1"
            chapter_files[chapter_name] = rpy_file
        
        return dict(sorted(chapter_files.items()))


def clean_text_for_tts(text: str) -> str:
    """Clean text for TTS generation by removing markup and formatting.
    
    Args:
        text: Raw text from .rpy file
        
    Returns:
        Cleaned text suitable for TTS
    """
    # Remove Ren'Py text tags
    text = re.sub(r'\{[^}]+\}', '', text)
    
    # Remove italics markers
    text = re.sub(r'\{i\}|\{/i\}', '', text)
    
    # Remove bold markers
    text = re.sub(r'\{b\}|\{/b\}', '', text)
    
    # Remove size tags
    text = re.sub(r'\{size=[^}]+\}|\{/size\}', '', text)
    
    # Remove color tags
    text = re.sub(r'\{color=[^}]+\}|\{/color\}', '', text)
    
    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()
