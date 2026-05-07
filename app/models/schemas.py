from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class VisionAssessment(BaseModel):
    damage_type: Optional[str] = None
    confidence: float = 0.0
    water_damage_visible: bool = False
    tampering_visible: bool = False
    image_quality: str = "unknown" 

class ClaimDecision(BaseModel):
    decision: Literal["approved", "rejected", "manual_review"]
    reason_codes: List[str] = Field(default_factory=list)
    confidence: float = 0.0

class UploadedEvidence(BaseModel):
    claim_id: str
    image_path: str

class ClaimWorkflowState(BaseModel):
    claim_id: str
    customer_statement: Optional[str] = None
    retrieved_clauses: List[dict] = Field(default_factory=list) 
    vision_assessment: Optional[VisionAssessment] = None
    missing_requirements: List[str] = Field(default_factory=list)
    final_decision: Optional[dict] = None

class ClaimSession(BaseModel):
    claim_id: str
    status: Literal["open", "awaiting_documents", "under_review"]
