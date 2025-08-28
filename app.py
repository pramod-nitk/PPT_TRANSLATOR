import streamlit as st
import os
import tempfile
from pathlib import Path
import time
from ppt_translator import PPTTranslator

# Page configuration
st.set_page_config(
    page_title="PPT Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🌐 PPT Translator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Upload your PowerPoint presentation and translate it into multiple languages</p>', unsafe_allow_html=True)
    
    # Sidebar for language selection
    with st.sidebar:
        st.header("🎯 Translation Settings")
        
        # Language selection
        st.subheader("Select Target Languages")
        
        # Available languages with their display names
        language_options = {
            "French": "fr",
            "German": "de", 
            "Spanish": "es",
            "Hindi": "hi",
            "Japanese": "ja",
            "Chinese (Simplified)": "zh-cn",
            "Russian": "ru",
            "Arabic": "ar",
            "Portuguese": "pt",
            "Italian": "it",
            "Korean": "ko",
            "Dutch": "nl",
            "Swedish": "sv",
            "Norwegian": "no",
            "Danish": "da",
            "Finnish": "fi",
            "Polish": "pl",
            "Turkish": "tr",
            "Greek": "el",
            "Hebrew": "he"
        }
        
        # Multi-select for languages
        selected_languages = st.multiselect(
            "Choose languages to translate to:",
            options=list(language_options.keys()),
            default=["French", "Spanish", "German"],
            help="Select one or more target languages for translation"
        )
        
        st.markdown("---")
        
        # Translation options
        st.subheader("⚙️ Options")
        auto_download = st.checkbox("Auto-download translated files", value=True)
        show_progress = st.checkbox("Show detailed progress", value=True)
        
        st.markdown("---")
        
        # Information
        st.subheader("ℹ️ Information")
        st.info("""
        **Supported formats:** .pptx files only
        
        **Translation service:** Google Translate
        
        **Note:** Large presentations may take several minutes to translate.
        """)

    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📤 Upload Presentation")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a PowerPoint file (.pptx)",
            type=['pptx'],
            help="Upload your PowerPoint presentation file"
        )
        
        if uploaded_file is not None:
            # Display file info
            file_details = {
                "Filename": uploaded_file.name,
                "File size": f"{uploaded_file.size / 1024:.2f} KB",
                "File type": uploaded_file.type
            }
            
            st.json(file_details)
            
            # Show preview of selected languages
            if selected_languages:
                st.subheader("🎯 Target Languages")
                lang_codes = [language_options[lang] for lang in selected_languages]
                st.write(f"Selected: {', '.join(selected_languages)}")
                st.write(f"Language codes: {', '.join(lang_codes)}")
            
            # Translation button
            if st.button("🚀 Start Translation", type="primary", use_container_width=True):
                if not selected_languages:
                    st.error("Please select at least one target language!")
                else:
                    # Initialize translator
                    translator = PPTTranslator()
                    
                    # Create progress bar
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # Create temporary directory for processing
                    with tempfile.TemporaryDirectory() as temp_dir:
                        # Save uploaded file
                        input_path = os.path.join(temp_dir, uploaded_file.name)
                        with open(input_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        
                        # Translate for each language
                        total_languages = len(selected_languages)
                        translated_files = []
                        
                        for i, lang_name in enumerate(selected_languages):
                            lang_code = language_options[lang_name]
                            
                            # Update progress
                            progress = (i / total_languages)
                            progress_bar.progress(progress)
                            status_text.text(f"Translating to {lang_name}... ({i+1}/{total_languages})")
                            
                            if show_progress:
                                st.info(f"🔄 Translating to {lang_name} ({lang_code})...")
                            
                            try:
                                # Generate output filename
                                base_name = Path(uploaded_file.name).stem
                                output_filename = f"{base_name}_{lang_code}.pptx"
                                output_path = os.path.join(temp_dir, output_filename)
                                
                                # Translate the presentation
                                translator.translate_presentation(input_path, output_path, lang_code)
                                
                                # Read the translated file for download
                                with open(output_path, "rb") as f:
                                    file_data = f.read()
                                
                                translated_files.append({
                                    "name": output_filename,
                                    "data": file_data,
                                    "language": lang_name,
                                    "size": len(file_data)
                                })
                                
                                if show_progress:
                                    st.success(f"✅ Successfully translated to {lang_name}")
                                
                            except Exception as e:
                                st.error(f"❌ Error translating to {lang_name}: {str(e)}")
                        
                        # Complete progress
                        progress_bar.progress(1.0)
                        status_text.text("Translation completed!")
                        
                        # Display results
                        st.markdown("---")
                        st.header("📥 Download Translated Files")
                        
                        if translated_files:
                            st.markdown('<div class="success-box">', unsafe_allow_html=True)
                            st.success(f"🎉 Successfully translated to {len(translated_files)} language(s)!")
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Create download buttons
                            for file_info in translated_files:
                                col1, col2, col3 = st.columns([3, 1, 1])
                                
                                with col1:
                                    st.write(f"**{file_info['language']}** - {file_info['name']}")
                                
                                with col2:
                                    st.write(f"{file_info['size'] / 1024:.1f} KB")
                                
                                with col3:
                                    st.download_button(
                                        label="📥 Download",
                                        data=file_info['data'],
                                        file_name=file_info['name'],
                                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                                        key=f"download_{file_info['language']}"
                                    )
                            
                            # Batch download option
                            if len(translated_files) > 1:
                                st.markdown("---")
                                st.subheader("📦 Batch Download")
                                
                                # Create a zip file with all translations
                                import zipfile
                                import io
                                
                                zip_buffer = io.BytesIO()
                                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                                    for file_info in translated_files:
                                        zip_file.writestr(file_info['name'], file_info['data'])
                                
                                zip_buffer.seek(0)
                                
                                st.download_button(
                                    label="📦 Download All Files (ZIP)",
                                    data=zip_buffer.getvalue(),
                                    file_name=f"{Path(uploaded_file.name).stem}_translations.zip",
                                    mime="application/zip",
                                    use_container_width=True
                                )
                        else:
                            st.error("No files were successfully translated.")
    
    with col2:
        st.header("📊 Statistics")
        
        if uploaded_file is not None:
            st.metric("File Size", f"{uploaded_file.size / 1024:.1f} KB")
            
            if selected_languages:
                st.metric("Target Languages", len(selected_languages))
                
                # Estimated time
                estimated_time = len(selected_languages) * 30  # 30 seconds per language
                st.metric("Estimated Time", f"{estimated_time // 60}m {estimated_time % 60}s")
        
        st.markdown("---")
        st.header("💡 Tips")
        st.info("""
        • For best results, use simple fonts
        • Avoid complex formatting
        • Keep text concise
        • Test with a small file first
        """)

if __name__ == "__main__":
    main()
