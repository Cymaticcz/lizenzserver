from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datei für Kundendaten
DATEI_NAME = "kunden.json"

# Kundendaten laden, falls Datei existiert
if os.path.exists(DATEI_NAME):
    with open(DATEI_NAME, "r", encoding="utf-8") as f:
        kunden_daten = json.load(f)
else:
    kunden_daten = []

# Speichern-Funktion
def speichere_kunden():
    with open(DATEI_NAME, "w", encoding="utf-8") as f:
        json.dump(kunden_daten, f, indent=4, ensure_ascii=False)

@app.post("/upload")
async def upload(request: Request):
    global kunden_daten
    kunden_daten = await request.json()
    speichere_kunden()
    return {"message": f"{len(kunden_daten)} Datensätze empfangen"}

@app.get("/download")
def download():
    return kunden_daten

@app.get("/")
def home():
    return {"message": "Server läuft ✅"}
