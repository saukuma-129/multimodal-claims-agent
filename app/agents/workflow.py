from app.models.schemas import ClaimWorkflowState
from app.claims_logic.engine import ClaimsDecisionEngine
from app.multimodal.analyzer import ClaimsEvidenceAnalyzer
from app.knowledge.store import PolicyStore

class ClaimWorkflow:
    def __init__(self):
        self.engine = ClaimsDecisionEngine()
        self.analyzer = ClaimsEvidenceAnalyzer()
        self.retriever = PolicyStore()

    def process_claim(self, state: ClaimWorkflowState, image_path: str) -> ClaimWorkflowState:
        # 1. RAG: Pull relevant policy text based on customer statement
        if state.customer_statement:
            state.retrieved_clauses = self.retriever.retrieve_relevant_clauses(
                state.customer_statement
            )

        # 2. Vision: Extract facts from image
        state.vision_assessment = self.analyzer.analyze_damage_image(image_path)

        # 3. Decision: Run policy engine with vision + rag data
        state.final_decision = self.engine.evaluate(state)
        
        return state
