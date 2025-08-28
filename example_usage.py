#!/usr/bin/env python3
"""
Example usage of the PPTTranslator class.

This script demonstrates how to use the PPTTranslator programmatically
for translating PowerPoint presentations.
"""

import os
from ppt_translator import PPTTranslator

def example_single_translation():
    """Example: Translate a presentation to a single language."""
    print("🌍 Example: Single Language Translation")
    print("-" * 40)
    
    # Initialize translator
    translator = PPTTranslator()
    
    # Example file paths (you'll need to provide your own)
    input_file = "example_presentation.pptx"  # Replace with your file
    output_file = "example_presentation_fr.pptx"
    target_language = "fr"  # French
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Input file '{input_file}' not found.")
        print("Please provide a valid PowerPoint file path.")
        return
    
    try:
        print(f"📤 Translating '{input_file}' to {target_language}...")
        translator.translate_presentation(input_file, output_file, target_language)
        print(f"✅ Translation completed! Output: {output_file}")
        
    except Exception as e:
        print(f"❌ Translation failed: {e}")

def example_multiple_languages():
    """Example: Translate a presentation to multiple languages."""
    print("\n🌍 Example: Multiple Language Translation")
    print("-" * 40)
    
    # Initialize translator
    translator = PPTTranslator()
    
    # Example file paths
    input_file = "example_presentation.pptx"  # Replace with your file
    output_dir = "translated_presentations"
    
    # Target languages
    languages = ["fr", "es", "de", "it"]  # French, Spanish, German, Italian
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Input file '{input_file}' not found.")
        print("Please provide a valid PowerPoint file path.")
        return
    
    try:
        print(f"📤 Translating '{input_file}' to {len(languages)} languages...")
        translated_files = translator.translate_multiple_languages(
            input_file, output_dir, languages
        )
        
        print(f"✅ Translation completed! {len(translated_files)} files created:")
        for file_path in translated_files:
            print(f"   📄 {os.path.basename(file_path)}")
            
    except Exception as e:
        print(f"❌ Translation failed: {e}")

def example_language_support():
    """Example: Show supported languages."""
    print("\n🌍 Example: Supported Languages")
    print("-" * 40)
    
    translator = PPTTranslator()
    languages = translator.get_supported_languages()
    
    print(f"📚 Total supported languages: {len(languages)}")
    print("\nAvailable languages:")
    
    # Display languages in a formatted way
    for i, (name, code) in enumerate(languages.items(), 1):
        print(f"{i:2d}. {name:<20} ({code})")

def example_language_normalization():
    """Example: Language code normalization."""
    print("\n🌍 Example: Language Code Normalization")
    print("-" * 40)
    
    translator = PPTTranslator()
    
    # Test various language inputs
    test_inputs = [
        "English",
        "en",
        "EN",
        "en-US",
        "French",
        "fr",
        "Spanish",
        "es"
    ]
    
    print("Language code normalization examples:")
    for lang_input in test_inputs:
        normalized = translator.normalize_lang(lang_input)
        print(f"  '{lang_input}' -> '{normalized}'")

def main():
    """Run all examples."""
    print("🚀 PPT Translator Examples")
    print("=" * 50)
    
    # Show supported languages
    example_language_support()
    
    # Show language normalization
    example_language_normalization()
    
    # Note about file requirements
    print("\n📝 Note:")
    print("To run the translation examples, you need to:")
    print("1. Provide a valid PowerPoint (.pptx) file")
    print("2. Update the file paths in the example functions")
    print("3. Ensure you have an internet connection for translation")
    
    # Uncomment the lines below to run actual translations
    # (after providing valid file paths)
    # example_single_translation()
    # example_multiple_languages()

if __name__ == "__main__":
    main()
