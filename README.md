# Playground-GenAI-CLI

Playground-GenAI-CLI is a command-line interface (CLI) tool for interacting with the OpenAI API, allowing users to have conversations with an AI model directly from the terminal. This project uses environment variables for configuration and relies on the Azure OpenAI service.

## Features
- Interact with an AI assistant from the terminal.
- Maintain conversational context between inputs and responses.
- Easily configurable via environment variables.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Requirements](#requirements)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Playground-GenAI-CLI.git
    cd Playground-GenAI-CLI
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    # or
    venv\Scripts\activate  # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Rename `.env.sample` to `.env` and provide your API key:
    ```bash
    mv .env.sample .env
    ```

    Open the `.env` file and update it with your actual API key:
    ```env
    API_ENDPOINT=https://api.groq.com/openai/v1
    API_KEY=your-api-key-here
    MODEL=llama-3.2-90b-text-preview
    ```

## Usage

To start interacting with the AI, simply run the script:

```bash
python main.py
```
The system will prompt you to enter text, and the AI assistant will respond. You can exit the program at any time by typing ``exit``.

Example:

```bash
You : Hello!
ERIOS Assistant : Hi there! How can I assist you today?
```

## Configuration

The project uses environment variables for configuration. These variables are stored in the .env file. The key settings are:

- `API_ENDPOINT`: The base URL for the OpenAI API.
- `API_KEY`: Your personal API key to authenticate requests.
- `MODEL`: The specific AI model you want to interact with (e.g., llama-3.2-90b-text-preview).

Make sure your .env file is correctly configured before running the project.

## Requirements

- Python 3.8+
- Dependencies listed in requirements.txt

To install the dependencies, run:
```bash
pip install -r requirements.txt
```