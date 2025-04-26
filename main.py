from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

kunden_daten = []

@app.post("/upload")
async def upload(request: Request):
    global kunden_daten
    kunden_daten = await request.json()
    return {"message": f"{len(kunden_daten)} Datensätze empfangen"}

@app.get("/download")
def download():
    return kunden_daten

@app.get("/")
def home():
    return {"message": "Server läuft ✔️"}

