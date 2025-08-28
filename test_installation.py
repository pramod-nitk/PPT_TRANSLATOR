#!/usr/bin/env python3
"""
Test script to verify PPT Translator installation and basic functionality.
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported."""
    print("🔍 Testing package imports...")
    
    required_packages = [
        'streamlit',
        'pptx',
        'googletrans',
        'langcodes',
        'PIL'
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Please install missing packages using: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_translator_module():
    """Test if the PPTTranslator module can be imported and initialized."""
    print("\n🔍 Testing PPTTranslator module...")
    
    try:
        from ppt_translator import PPTTranslator
        translator = PPTTranslator()
        print("✅ PPTTranslator imported and initialized successfully!")
        
        # Test language normalization
        test_lang = translator.normalize_lang("en")
        print(f"✅ Language normalization test: 'en' -> '{test_lang}'")
        
        # Test supported languages
        languages = translator.get_supported_languages()
        print(f"✅ Supported languages: {len(languages)} languages available")
        
        return True
        
    except Exception as e:
        print(f"❌ PPTTranslator test failed: {e}")
        return False

def test_streamlit_app():
    """Test if the Streamlit app can be imported."""
    print("\n🔍 Testing Streamlit app...")
    
    try:
        import app
        print("✅ Streamlit app imported successfully!")
        return True
    except Exception as e:
        print(f"❌ Streamlit app test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 PPT Translator Installation Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_translator_module,
        test_streamlit_app
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your installation is ready.")
        print("\n🚀 To run the application:")
        print("   streamlit run app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
