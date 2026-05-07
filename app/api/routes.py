import os
from fastapi import APIRouter, HTTPException
from app.models.schemas import UploadedEvidence, VisionAssessment
from app.multimodal.analyzer import ClaimsEvidenceAnalyzer

router = APIRouter()
evidence_analyzer = ClaimsEvidenceAnalyzer()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.post("/claims/analyze-image", response_model=VisionAssessment)
async def analyze_claim_image(uploaded_evidence: UploadedEvidence):
    if not os.path.exists(uploaded_evidence.image_path):
        raise HTTPException(status_code=404, detail="Evidence file not found")
    
    try:
        return evidence_analyzer.analyze_damage_image(uploaded_evidence.image_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
