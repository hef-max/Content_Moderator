from fastapi import FastAPI
from app.schemas import TextInput
from app.predictor import predict_toxicity, classify_topic
from app.model_loader import load_toxicity_model
from app.logger import log_toxic
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

app = FastAPI()

tox_tokenizer, tox_model = load_toxicity_model()

# Serve folder `frontend/` di root
# app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Fallback: ketika akses root "/", tampilkan index.html
@app.get("/")
def root():
    return FileResponse("frontend/index.html")

@app.post("/moderate")
def moderate_text(input: TextInput):
    score, is_toxic = predict_toxicity(input.text, tox_tokenizer, tox_model)
    category = classify_topic(input.text)
    if is_toxic:
        log_toxic(input.text, score)
    return {
        "text": input.text,
        "toxicity_score": round(score, 3),
        "is_toxic": is_toxic,
        "category": category
    }
