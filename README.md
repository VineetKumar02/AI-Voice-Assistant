# Voice Assistant - Your Personal AI Companion

Welcome to the **Voice Assistant** project! This Python-based voice assistant utilizes speech recognition, text-to-speech technologies, and Google's Bard AI to understand voice commands and provide responses.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Introduction

The **Voice Assistant** project brings the convenience of voice commands to your fingertips. Whether you want to inquire about the weather, ask questions, or get tasks done, this assistant is here to help.

## Features

- Voice recognition and command execution.
- Text-to-speech responses for interactive communication.
- Integration with Google's Bard AI for context-aware responses.
- Customizable voice commands and actions.

## Getting Started

To get started with the project, follow these steps:

### 1. Get Source Code Files
#### Option 1: Clone Repository

- If you have Git installed, you can clone the repository using the following command:

  ```bash
  git clone https://github.com/VineetKumar02/Python-Voice-Assistant.git
  ```

- After cloning, navigate to the project directory:

  ```bash
  cd Python-Voice-Assistant
  ```

#### Option 2: Download ZIP

- If you prefer not to use Git, you can download the ZIP archive of the project:

  1. Click the "Code" button on the repository page.
  2. Choose "Download ZIP."
  3. Extract the downloaded ZIP file to a location of your choice.

### 2. Install Dependencies

Install the required Python libraries using pip:

1. Using Reqirements.txt file
    ```bash
    pip install -r requirements.txt
    ```

    or

2. For latest version of packages (May not work. If fails.. Follow method 1)

    ```bash
    pip install pyttsx3 speech_recognition google-generativeai python-dotenv pyaudio
    ```

### 3. API Configuration

- Create a Google Bard AI account and obtain an API key.
- Configure your `.env` file with your API key:

  ```
  PALM_API_KEY=YOUR_API_KEY
  ```

### 4. Run the Assistant

  Execute the python script to start the voice assistant:

  ```bash
  python bardai.py
  ```

## Usage

- Begin interacting with the voice assistant by saying "Hello Jarvis" or your preferred wake-up phrase.
- Ask questions, give commands, or engage in casual conversations.
- Use the command "Shutdown Jarvis" to exit the assistant.

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- Google's Bard AI

## Contributing

Contributions to this project are welcome! Feel free to open issues and submit pull requests for any enhancements or fixes.

**Note:** This project is for educational and demonstration purposes. Make sure to follow ethical guidelines and respect user privacy when creating voice assistant applications.