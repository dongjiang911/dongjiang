from datetime import datetime, timezone
from typing import Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="FarmSense IoT API", version="1.0.0")

latest: Dict[str, Dict[str, Any]] = {}
history: list[Dict[str, Any]] = []

class Telemetry(BaseModel):
    deviceId: str = Field(min_length=1)
    timestamp: datetime
    metrics: Dict[str, float]

@app.get("/api/v1/health")
def health():
    return {"status": "ok", "devices": len(latest)}

@app.post("/api/v1/sensors/telemetry")
def ingest(payload: Telemetry):
    record = payload.model_dump()
    latest[payload.deviceId] = record
    history.append(record)
    return {"ok": True, "deviceId": payload.deviceId, "receivedAt": datetime.now(timezone.utc).isoformat()}

@app.get("/api/v1/sensors/latest")
def get_latest():
    return {"data": list(latest.values())}

@app.get("/api/v1/sensors/history")
def get_history(deviceId: str | None = None):
    data = [x for x in history if not deviceId or x["deviceId"] == deviceId]
    return {"data": data[-500:]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
