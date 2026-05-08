# AI Usage & Strategic Overrides

This project utilized LLMs for boilerplate generation and initial Pydantic schema drafting, but I manually overrode the architecture in three critical areas to ensure reliability and production safety:

1. **Rejection of "Agentic Decisioning":** I explicitly blocked the LLM from having the final "Approve/Reject" authority. Initial AI suggestions favored a "Chat-to-Decision" flow, which is non-deterministic and un-auditable. I replaced this with a deterministic Python engine to ensure consistent policy enforcement.

2. **Constrained JSON Extraction:** I moved away from free-form vision summaries in favor of a strict classification schema. This prevents "description drift" where the AI describes damage differently across multiple runs, ensuring stable inputs for the rules engine.

3. **Manual Review & Safety Fallbacks:** I manually implemented the "Low Confidence" and "Thermal Damage" routing logic. AI models tend toward over-confidence; these human-in-the-loop gates were required to handle edge cases like blurry images or high-liability hardware failures (burns/fire).
