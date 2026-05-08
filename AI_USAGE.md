# AI Usage & Strategic Overrides

This project utilized LLMs for boilerplate generation and initial Pydantic schema drafting, but I manually overrode the architecture in two critical areas to ensure reliability:

1. **Rejection of "Agentic Decisioning":** I explicitly blocked the LLM from having the final "Approve/Reject" authority. Initial AI suggestions favored a "Chat-to-Decision" flow, which is un-auditable. I replaced this with a deterministic Python engine.
2. **Constrained JSON Extraction:** I moved away from free-form vision summaries to a strict classification schema. This prevents "description drift" where the AI describes damage differently every time.
3. **Manual Review Fallbacks:** I manually implemented the "Low Confidence" routing logic. AI tends to be "over-confident"; the fallback logic was a human-in-the-loop requirement to handle edge cases like blurry receipts.
