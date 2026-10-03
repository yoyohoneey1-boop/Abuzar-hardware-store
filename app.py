# Optional AI backend for the same website.
# GitHub Pages cannot run Python; use this file only if you deploy the backend
# on a Python host (Render/Railway/VPS/etc.) and point the frontend to its /api/chat.

import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")
SYSTEM = """You are the Abuzar Aluminium & Glass Hardware store assistant.
Help customers with aluminium profiles, glass hardware, door hardware, handles,
locks, shower hardware, project requirements, product specifications and quote requests.
Be concise, polite, practical and never invent stock or prices. If current pricing,
availability or delivery is requested, ask for the product, quantity, specification
and city, then say the store team should confirm it."""

@app.get("/")
def home():
    return send_from_directory(".", "index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"reply":"Please type your question."})
    # Optional OpenAI integration:
    # pip install openai
    # Set OPENAI_API_KEY on the server and uncomment the block below.
    try:
        from openai import OpenAI
        key = os.environ.get("OPENAI_API_KEY")
        if key:
            client = OpenAI(api_key=key)
            r = client.responses.create(
                model=os.environ.get("OPENAI_MODEL","gpt-5-mini"),
                instructions=SYSTEM,
                input=message
            )
            return jsonify({"reply": r.output_text})
    except Exception:
        pass
    return jsonify({"reply":"I can help with glass hardware, aluminium profiles, handles, locks, quotations and project requirements. Please share the product, quantity and specification."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
