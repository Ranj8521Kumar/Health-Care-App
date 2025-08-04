# Health Care App - Plant Disease Detection

A Flask-based web application that combines plant disease detection using TensorFlow with an AI chatbot powered by OpenAI GPT.

---

## 🌟 App Screenshot

<!-- Replace the link below with your actual screenshot when available -->
<p align="center">
  <img src="app_screenshot_placeholder.png" alt="App Screenshot" width="600"/>
</p>

---

## Features

- Plant disease detection using pre-trained TensorFlow model
- AI chatbot for plant disease consultation using OpenAI GPT
- Modern, responsive web interface:
  - **Desktop:** Navbar at the top, description panel on the left, chatbot on the right
  - **Mobile:** Navbar at the top, description at the top, chatbot below
- Easy image upload and instant feedback

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (for chatbot functionality)

## Setup Instructions

### Option 1: Using PowerShell (Recommended)
```powershell
.\setup.ps1
```

### Option 2: Using Command Prompt
```cmd
setup.bat
```

### Option 3: Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate.bat
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Environment Variables

Before running the app, set your OpenAI API key:

### Windows (Command Prompt)
```cmd
set OPENAI_API_KEY=your_api_key_here
```

### Windows (PowerShell)
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### macOS/Linux
```bash
export OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate.bat

   # macOS/Linux
   source venv/bin/activate
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to: `http://localhost:5000`

## Usage

1. **Plant Disease Detection:** Upload an image of a plant leaf to detect diseases.
2. **AI Chatbot:** Ask questions about plant diseases and treatments.
3. **Modern UI:** 
   - On desktop, you'll see a navigation bar, a description panel on the left, and the chatbot on the right.
   - On mobile, the description appears at the top and the chatbot below for easy access.

## Dependencies

- Flask: Web framework
- OpenAI: AI chatbot integration
- Pillow: Image processing
- NumPy: Numerical computing
- TensorFlow: Machine learning framework
- TensorFlow Hub: Pre-trained models

## Note

Make sure you have a valid OpenAI API key for the chatbot functionality to work properly. 