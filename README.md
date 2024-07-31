# Voice-Assistant
# This is project for internship
# Voice Assistant

## Description

This project is a simple voice assistant that can respond to greetings, tell the current time and date, and perform Wikipedia searches. It leverages the `SpeechRecognition` library for voice recognition, `pyttsx3` for text-to-speech functionality, and `wikipedia` for retrieving information.

## Features

- Responds to user greetings.
- Provides the current time.
- Provides today's date.
- Searches Wikipedia and reads out summaries.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

To set up and run the voice assistant, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/voice-assistant.git
    cd voice-assistant
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the voice assistant with the following command:

```bash
python src/main.py
