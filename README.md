# AI CUSTOMER SUPPORT CHATBOT
==========================

## Description:
------------
A Python-based AI chatbot with graphical user interface (GUI) for customer support applications. 
Uses Hugging Face Transformers for natural language processing and Tkinter for the interface.

## Features:
---------
- User-friendly GUI built with Tkinter
- Powered by pre-trained AI models (DialoGPT-small or DistilGPT2)
- Real-time conversation display
- Error handling and status indicators
- Easy to extend with custom training data

## Requirements:
-------------
- Python 3.8 or higher
- PyTorch (torch)
- Transformers library
- Tkinter (usually included with Python)

## Installation:
-------------
1. Clone the repository:
   git clone https://github.com/yourusername/customer-support-chatbot.git

2. Navigate to project directory:
   cd customer-support-chatbot

3. Install dependencies:
   pip install -r requirements.txt

## Usage:
------
Run the chatbot:
python chatbot_gui.py

Keyboard Shortcuts:
- Enter: Send message
- Ctrl+C: Exit program

## Configuration:
--------------
You can modify these settings in chatbot_gui.py:
- Change AI model: Edit model="microsoft/DialoGPT-small"
- Adjust response length: Modify max_length=100
- Change window size: Update geometry("800x600")

## Troubleshooting:
----------------
1. Model download issues:
   - Check internet connection
   - Try smaller model (distilgpt2)
   - Clear cache: rm -r ~/.cache/huggingface

2. GUI not responding:
   - Ensure Tkinter is installed
   - Run as administrator (Windows)

3. Performance problems:
   - Reduce max_length parameter
   - Use CPU-only mode (add device="cpu" to pipeline)

## Files Included:
---------------
- chatbot_gui.py : Main application script
- requirements.txt : Dependency list
- README.txt : This documentation

## License:
--------
MIT License - Free for educational and commercial use

## Contact:
--------
Sri Harsha M

sriharsha0413@gmail.com

Project URL: https://github.com/yourusername/customer-support-chatbot

## Version History:
---------------
1.0 (2023-11-15) - Initial release
1.1 (2023-11-20) - Added error handling
