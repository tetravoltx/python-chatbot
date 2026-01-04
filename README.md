# Terminal Chatbot

A minimalist, terminal-inspired desktop chatbot application built with Python and Tkinter, powered by Google's Gemini AI.

![Terminal Chatbot Interface](https://github.com/user-attachments/assets/ee0968c5-7c48-437b-8abd-aec887617cc7)

## Features

- **Terminal-Inspired Interface** - Clean, minimalist black & white design with Linux command-line aesthetics
- **Google Gemini Integration** - Powered by Gemini 2.5 Flash for intelligent responses
- **Keyboard-Driven** - Press Enter to send, Shift+Enter for new lines
- **Monospace Typography** - JetBrains Mono/Consolas fonts for that authentic terminal feel
- **Session Management** - Start new chat sessions with a single click
- **Error Handling** - Graceful error messages for API issues
- **Lightweight** - No heavy dependencies, runs on pure Python + Tkinter

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Gemini API key (free from Google AI Studio)

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/tetravoltx/python-chatbot.git
cd python-chatbot
```

### 2. Install Dependencies
```bash
pip install google-generativeai python-dotenv
```

### 3. Get a Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key

### 4. Configure Environment Variables
Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
python app.py
```

## Usage

1. Launch the application with `python app.py`
2. Type your message in the input field at the bottom
3. Press `Enter` to send
4. Use `Shift + Enter` for multi-line input
5. Click "New Chat" to start a fresh conversation

## Project Structure

```
python-chatbot/
│
├── app.py              # Main GUI application (Tkinter interface)
├── ai_logic.py         # Gemini API integration and AI logic
├── .env                # Environment variables (API keys - not tracked)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation (this file)
```

## Usage

### Basic Commands

- **Send Message**: Type your message and press `Enter`
- **New Line**: Press `Shift + Enter` to add a new line without sending
- **New Chat**: Click the refresh icon (⟳) to start a fresh conversation

### Example Interactions

```
user@gemini:~$ What is Python?
Python is a high-level, interpreted programming language...
```

```
user@gemini:~$ Write a hello world program
print("Hello, World!")
```

### Customization

You can customize the appearance by modifying these variables in `app.py`:

```python
BG = "#0a0a0a"           # Background color
FG = "#e8e8e8"           # Foreground text color
ACCENT = "#ffffff"       # Accent color
FONT_MAIN = "JetBrains Mono"  # Main font
```

## Known Issues

### API Rate Limits
The free tier of Gemini API has rate limits:

- **Limit**: 20 requests per day for `gemini-2.5-flash`
- **Solution**: Wait for the cooldown period or switch to `gemini-1.5-flash` in `ai_logic.py`

### Font Availability
If your system doesn't have JetBrains Mono or Consolas, the app will fallback to Arial. For the best experience:

- **Windows**: Consolas comes pre-installed
- **Mac**: [Download JetBrains Mono](https://www.jetbrains.com/lp/mono/)
- **Linux**: Install via package manager:
  ```bash
  sudo apt install fonts-jetbrains-mono
  ```
