# Simple Chatbot

A lightweight AI chatbot built with FastAPI and the OpenAI API.  
This project demonstrates how to build and run a simple AI-powered backend with a minimal web interface.

---

## Features

- FastAPI backend
- Simple browser-based UI
- OpenAI-powered responses
- Clean and minimal setup
- Easy to extend (chat history, RAG, etc.)

---

## Project Structure

```
simple-chatbot/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.10+
- OpenAI API key

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/pydev-y/simple-chatbot
cd simple-chatbot
```

---

### 2. Create virtual environment

**Windows**
```bash
python -m venv env
```

**Linux / macOS**
```bash
python3 -m venv env
```

---

### 3. Activate environment

**Windows**
```bash
env\Scripts\activate
```

**Linux / macOS**
```bash
source env/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

Example:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

> Do not upload your `.env` file to GitHub.

---

## Run the Application

```bash
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## API Usage

### Endpoint

```
POST /chat
```

### Example

```
http://127.0.0.1:8000/chat?message=Hello
```

---

## Common Issues

**Missing API key**
- Ensure `.env` file exists
- Ensure `OPENAI_API_KEY` is set correctly

**Module not found**
- Activate virtual environment
- Run `pip install -r requirements.txt`

**Port already in use**
```bash
uvicorn app:app --reload --port 8001
```

---

## Future Improvements

- Chat history
- Streaming responses
- Custom system prompts
- RAG (document-based chatbot)
- Database integration
- UI improvements

---

## License

This project is open-source and available for learning and experimentation.
