from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Community Health Extension Registry API")

class PatientRecord(BaseModel):
    patient_name: str
    woreda: str
    muac_cm: float
    service_type: str = "Nutritional Screening"

@app.get("/health")
def health():
    return {"status": "ok", "location": "Semera, Afar, Ethiopia"}

@app.post("/sync")
def sync_records(records: List[PatientRecord]):
    return {"status": "synced", "received_count": len(records)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
