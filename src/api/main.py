from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Safety Detector API")

class DetectRequest(BaseModel):
    camera_id: str
    frame_url: str

@app.post("/detect")
def detect(req: DetectRequest):
    # В реальной системе здесь будет анализ кадра моделью CV
    return {
        "camera_id": req.camera_id,
        "timestamp": "2025-04-11T14:35:22Z",
        "detected_objects": ["person", "knife"],
        "situation": "weapon_detected",
        "risk_level": "critical",
        "confidence": 0.92
    }