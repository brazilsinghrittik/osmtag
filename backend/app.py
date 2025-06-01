# app.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)) -> List[str]:
    # Dummy prediction — replace with ML later
    return [
        "highway=residential",
        "surface=asphalt",
        "sidewalk=both"
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

