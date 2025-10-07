#!/usr/bin/env python3
"""
Quick test of the Care Emoji Generator web app
"""
import sys
import os
from PIL import Image

# Add the web directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'web'))

from emojiGenerator import EmojiGenerator

def test_emoji_generation():
    """Test the emoji generation with a simple test image"""
    print("Testing Care Emoji Generator...")
    
    # Create a simple test image
    test_img = Image.new('RGB', (200, 200), color='red')
    
    # Generate the emoji
    eg = EmojiGenerator()
    result_img = eg.generateCareEmoji(test_img)
    
    # Save the result
    output_path = os.path.join(os.path.dirname(__file__), 'test_output.png')
    result_img.save(output_path)
    
    print(f"✅ Emoji generation successful!")
    print(f"Test output saved to: {output_path}")
    print(f"Result image size: {result_img.size}")
    
    return True

if __name__ == '__main__':
    try:
        test_emoji_generation()
        print("\n🎉 Web app is ready to use!")
        print("Open your browser to http://localhost:5337 to start generating care emojis!")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)