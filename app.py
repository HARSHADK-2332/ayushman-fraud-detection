from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def detect_fraud(file: UploadFile = File(...)):
    
    risk_score = random.randint(10,95)

    if risk_score > 70:
        label = "High Fraud Risk"
    elif risk_score > 40:
        label = "Medium Risk"
    else:
        label = "Low Risk"

    return {
        "risk_score": risk_score,
        "risk_label": label
    }