"""Sink server – receives ChatGPT conversation payloads from a Chrome extension."""

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

app = FastAPI(title="ChatGPT Sink")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class ConversationPayload(BaseModel):
    fetched_at: str
    conversation_id: str
    label: str
    payload: dict


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chatgpt")
async def receive(body: ConversationPayload, request: Request):
    auth = request.headers.get("authorization")
    if auth:
        log.info("Auth header present: %s…", auth[:20])

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")
    size = len(json.dumps(body.payload))
    log.info("recv conversation_id=%s label=%s payload_chars=%d", body.conversation_id, body.label, size)

    fname = f"{body.conversation_id}_{ts}.json"
    (DATA_DIR / fname).write_text(json.dumps(body.model_dump(), indent=2))

    return {"saved": fname}


@app.get("/conversations")
def list_conversations():
    results = []
    for p in sorted(DATA_DIR.glob("*.json")):
        try:
            data = json.loads(p.read_text())
            results.append({
                "conversation_id": data.get("conversation_id"),
                "label": data.get("label"),
                "fetched_at": data.get("fetched_at"),
                "file": p.name,
            })
        except Exception:
            results.append({"file": p.name, "error": "unreadable"})
    return results


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8484"))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
