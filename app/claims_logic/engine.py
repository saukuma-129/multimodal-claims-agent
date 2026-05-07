from app.models.schemas import ClaimDecision, ClaimWorkflowState

class ClaimsDecisionEngine:
    def evaluate(self, state: ClaimWorkflowState) -> ClaimDecision:
        v = state.vision_assessment

        if not v:
            return ClaimDecision(
                decision="manual_review", 
                reason_codes=["MANUAL_REVIEW_REQUIRED"]
            )

        if v.tampering_visible:
            return ClaimDecision(decision="rejected", reason_codes=["VOID_TAMPERING"], confidence=v.confidence)
        
        if v.water_damage_visible:
            return ClaimDecision(decision="rejected", reason_codes=["VOID_ENVIRONMENTAL_ABUSE"], confidence=v.confidence)

        is_high_quality = v.image_quality.lower() in ["good", "high", "excellent"]

        # If quality is poor or confidence is low, fall back to manual review
        if not is_high_quality or v.confidence < 0.60:
            return ClaimDecision(
                decision="manual_review", 
                reason_codes=["MANUAL_REVIEW_REQUIRED"],
                confidence=v.confidence
            )

        return ClaimDecision(
            decision="approved", 
            reason_codes=["STANDARD_APPROVAL"],
            confidence=v.confidence
        )
