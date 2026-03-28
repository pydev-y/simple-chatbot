import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI(title="Simple Chatbot")

api_key = os.getenv("OPENAI_API_KEY", "")
model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

client = OpenAI(api_key=api_key)

HTML_PAGE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Simple Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 760px; margin: 40px auto; padding: 0 16px; }
        h1 { margin-bottom: 8px; }
        p { color: #444; }
        textarea { width: 100%; height: 120px; padding: 12px; font-size: 16px; }
        button { margin-top: 12px; padding: 10px 16px; font-size: 16px; cursor: pointer; }
        .box { margin-top: 20px; padding: 16px; border: 1px solid #ddd; border-radius: 10px; white-space: pre-wrap; }
        .label { font-size: 14px; color: #666; margin-bottom: 8px; }
    </style>
</head>
<body>
    <h1>Simple Chatbot</h1>
    <p>Ask a question and get an AI response.</p>
    <form method="post" action="/chat-page">
        <textarea name="message" placeholder="Type your message here..."></textarea>
        <br>
        <button type="submit">Send</button>
    </form>
</body>
</html>
"""


def ask_model(user_message: str) -> str:
    if not api_key:
        return "Missing OPENAI_API_KEY. Add it to your .env file first."

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Keep answers clear and concise.",
            },
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
        max_tokens=300,
    )
    return response.choices[0].message.content or "No response returned."


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return HTML_PAGE


@app.post("/chat")
def chat(message: str):
    reply = ask_model(message)
    return JSONResponse({"reply": reply})



@app.post("/chat-page", response_class=HTMLResponse)
def chat_page(message: str = Form(...)) -> str:
    reply = ask_model(message)
    return f"""
    <!doctype html>
    <html>
    <head>
        <meta charset=\"utf-8\" />
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
        <title>Simple Chatbot</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 760px; margin: 40px auto; padding: 0 16px; }}
            textarea {{ width: 100%; height: 120px; padding: 12px; font-size: 16px; }}
            button {{ margin-top: 12px; padding: 10px 16px; font-size: 16px; cursor: pointer; }}
            .box {{ margin-top: 20px; padding: 16px; border: 1px solid #ddd; border-radius: 10px; white-space: pre-wrap; }}
            .label {{ font-size: 14px; color: #666; margin-bottom: 8px; }}
        </style>
    </head>
    <body>
        <h1>Simple Chatbot</h1>
        <form method=\"post\" action=\"/chat-page\">
            <textarea name=\"message\" placeholder=\"Type your message here...\">{message}</textarea>
            <br>
            <button type=\"submit\">Send</button>
        </form>

        <div class=\"box\">
            <div class=\"label\">Bot reply</div>
            {reply}
        </div>
    </body>
    </html>
    """