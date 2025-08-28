# 🌐 PPT Translator

A modern Streamlit web application for translating PowerPoint presentations into multiple languages using Google Translate.

## ✨ Features

- **📤 Easy Upload**: Drag and drop PowerPoint (.pptx) files
- **🌍 Multi-Language Support**: Translate to 20+ languages including French, German, Spanish, Hindi, Japanese, Chinese, Russian, Arabic, and more
- **⚡ Real-time Progress**: See translation progress with detailed status updates
- **📥 Instant Download**: Download individual translated files or batch download as ZIP
- **🎨 Modern UI**: Beautiful, responsive interface with intuitive controls
- **🔄 Retry Mechanism**: Automatic retry on translation failures
- **📊 Statistics**: File size, estimated time, and translation statistics

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd ppt_translator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📖 Usage

### Step 1: Upload Presentation
- Click "Browse files" or drag and drop your PowerPoint (.pptx) file
- The app will display file details including size and type

### Step 2: Select Languages
- In the sidebar, choose one or more target languages from the dropdown
- You can select multiple languages for batch translation

### Step 3: Configure Options
- **Auto-download**: Automatically download files when translation completes
- **Show detailed progress**: Display step-by-step translation progress

### Step 4: Start Translation
- Click the "🚀 Start Translation" button
- Monitor progress with the progress bar and status updates
- Wait for completion (typically 30-60 seconds per language)

### Step 5: Download Results
- Download individual translated files using the download buttons
- Or download all files as a ZIP archive for convenience

## 🌍 Supported Languages

| Language | Code | Language | Code |
|----------|------|----------|------|
| French | fr | German | de |
| Spanish | es | Hindi | hi |
| Japanese | ja | Chinese (Simplified) | zh-cn |
| Russian | ru | Arabic | ar |
| Portuguese | pt | Italian | it |
| Korean | ko | Dutch | nl |
| Swedish | sv | Norwegian | no |
| Danish | da | Finnish | fi |
| Polish | pl | Turkish | tr |
| Greek | el | Hebrew | he |

## 🏗️ Project Structure

```
ppt_translator/
├── app.py                 # Main Streamlit application
├── ppt_translator.py      # Core translation module
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── convert_ppt.py        # Original script (for reference)
```

## 🔧 Technical Details

### Core Components

- **`app.py`**: Streamlit web interface with file upload, language selection, and download functionality
- **`ppt_translator.py`**: Refactored translation engine with proper class structure
- **Google Translate API**: Used for text translation via `googletrans` library
- **python-pptx**: Handles PowerPoint file manipulation

### Key Features

- **Error Handling**: Robust error handling with retry mechanisms
- **Memory Efficient**: Processes files in temporary directories
- **Batch Processing**: Translates multiple languages simultaneously
- **Progress Tracking**: Real-time progress updates and status messages

## 💡 Tips for Best Results

1. **File Format**: Use .pptx files only (not .ppt)
2. **Fonts**: Use simple, widely-supported fonts
3. **Formatting**: Avoid complex formatting that might not translate well
4. **Text Length**: Keep text concise for better translation quality
5. **Testing**: Start with a small presentation to test the process

## 🐛 Troubleshooting

### Common Issues

1. **Translation Fails**
   - Check your internet connection
   - Try again with fewer languages selected
   - Ensure the PowerPoint file is not corrupted

2. **Download Issues**
   - Clear browser cache
   - Try downloading individual files instead of ZIP
   - Check available disk space

3. **Performance Issues**
   - Large files may take longer to process
   - Reduce the number of target languages
   - Close other applications to free up memory

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on the project repository.

---

**Note**: This application uses Google Translate service. Translation quality may vary depending on the complexity of the text and language pairs.
# PPT_TRANSLATOR
