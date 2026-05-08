from app.models.schemas import ClaimDecision, ClaimWorkflowState

class ClaimsDecisionEngine:
    def evaluate(self, state: ClaimWorkflowState) -> ClaimDecision:
        v = state.vision_assessment
        refs = [c["clause_id"] for c in state.retrieved_clauses]

        if not v:
            return ClaimDecision(
                decision="manual_review", 
                reason_codes=["MANUAL_REVIEW_REQUIRED"],
                policy_references=refs
            )
        
                # Safeguard: Don't approve if the policy search failed
        if not state.retrieved_clauses:
            return ClaimDecision(
                decision="manual_review", 
                reason_codes=["POLICY_CONTEXT_MISSING"]
            )

        if v.tampering_visible:
            return ClaimDecision(decision="rejected", reason_codes=["VOID_TAMPERING"], confidence=v.confidence, policy_references=refs)
        
        if v.water_damage_visible:
            return ClaimDecision(decision="rejected", reason_codes=["VOID_ENVIRONMENTAL_ABUSE"], confidence=v.confidence, policy_references=refs)

        is_high_quality = v.image_quality.lower() in ["good", "high", "excellent"]

        if not is_high_quality or v.confidence < 0.60:
            return ClaimDecision(
                decision="manual_review", 
                reason_codes=["MANUAL_REVIEW_REQUIRED"],
                confidence=v.confidence,
                policy_references=refs
            )

        return ClaimDecision(
            decision="approved", 
            reason_codes=["STANDARD_APPROVAL"],
            confidence=v.confidence,
            policy_references=refs
        )
