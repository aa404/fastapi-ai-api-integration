# Quick Integration of OpenAI, Gemini, and Claude APIs with FastAPI

This repository provides a quick and seamless integration of the OpenAI, Gemini, and Claude APIs using the FastAPI framework.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **OpenAI Integration**: Easily integrate with OpenAI's GPT models.
- **Gemini API**: Access Gemini's unique AI capabilities.
- **Claude API**: Utilize Claude's AI tools.
- **FastAPI Framework**: Leverage FastAPI for high performance and ease of use.
- **Asynchronous Support**: Fully asynchronous operations for high performance.

## Requirements

- Python 3.8+
- FastAPI
- HTTPX (for asynchronous HTTP requests)
- OpenAI Python client
- Gemini API client
- Claude API client

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/aa404/fastapi-ai-api-integration.git
    cd fastapi-ai-api-integration
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Rename `.env.example` to `.env` and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    GEMINI_API_KEY=your_gemini_api_key
    CLAUDE_API_KEY=your_claude_api_key
    ```

## Usage

1. **Run the FastAPI application**:
    ```bash
    fastapi dev
    ```

2. **Access the API documentation**:
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation provided by Swagger UI.

## API Endpoints

### OpenAI

- `POST /openai`
    - **Description**: Query OpenAI's GPT model.
    - **Request Body**:
        ```json
        {
            "message": "Your prompt here"
        }
        ```
    - **Response**:
        ```json
        {
            "response": "OpenAI's response"
        }
        ```

### Gemini

- `POST /gemini`
    - **Description**: Query Gemini's API.
    - **Request Body**:
        ```json
        {
            "message": "Your input here"
        }
        ```
    - **Response**:
        ```json
        {
            "response": "Gemini's response"
        }
        ```

### Claude

- `POST /claude`
    - **Description**: Query Claude's API.
    - **Request Body**:
        ```json
        {
            "message": "Your query here"
        }
        ```
    - **Response**:
        ```json
        {
            "response": "Claude's response"
        }
        ```

## Configuration

- **Environment Variables**: Configure your API keys and other settings in the `.env` file.
- **Logging**: Modify logging settings in `main.py`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

---
