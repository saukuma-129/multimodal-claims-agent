# Architecture: VoltEdge Claims Engine

## Decision Framework
The system is built on a **Hybrid Separation of Concerns**. We deliberately avoid the "Autonomous Agent" black-box pattern to ensure every warranty decision is legally auditable and consistent.

1.  **Stochastic Perception:** We use GPT-4o-mini to extract visual facts (e.g., `water_damage: true`, `image_quality: "high"`) into a structured Pydantic schema. This layer identifies *what* is in the image but has no authority to decide the claim outcome.
2.  **Deterministic Enforcement:** A Python-based `RulesEngine` consumes the extracted facts and matches them against the VoltEdge policy.
3.  **Rule Priority Queue:** To handle conflicting evidence, we enforce a strict priority list for rejections:
    *   `VOID_TAMPERING` (Highest legal priority)
    *   `VOID_ENVIRONMENTAL_ABUSE` (Water damage)
    *   `IMAGE_QUALITY_INSUFFICIENT` (System safeguard)
    *   `AMBIGUOUS_BURN_DAMAGE` (Safety/Liability gate)
    *   `MANUAL_REVIEW_REQUIRED` (Human fallback)

### Safety & Liability Gating
A critical architectural override was implemented for fire and thermal damage. While a naive AI might auto-approve "burnt wires" as a hardware failure, our engine treats all thermal events as high-risk. These are programmatically routed to `manual_review` to determine the root cause (internal component failure vs. external environmental abuse), mitigating safety liability.

## Human-in-the-Loop (HITL) Fallback
The system is not "fully autonomous" by design. Any claim with a visual confidence score below **0.75** or an ambiguous policy match is automatically routed to a `manual_review` state. We utilize a standardized `ReviewTask` schema to preserve the full system state—including extraction facts and the specific RAG-retrieved policy clauses—allowing a human auditor to verify the claim in seconds without re-processing.

## Production Scaling (1M+ Users)
*   **Asynchronous Orchestration:** The current workflow is synchronous for prototype simplicity. In production, multimodal inference (OpenAI) would be offloaded to **Celery/Redis** task queues to prevent high-latency GPU workloads from blocking the FastAPI event loop.
*   **Gateway Throttling:** We propose API-level rate limiting at the ingress layer. This protects expensive multimodal inference paths from "retry storms" and cost spikes during bursts of high-traffic or abuse.
*   **Vector Sharding:** ChromaDB handles our current policy base. For a 1M+ user scale, we would migrate to a managed **PGVector** instance, sharding policy embeddings by product SKU or region to maintain retrieval latency under 100ms.
*   **Tiered Model Routing:** To optimize COGS (Cost of Goods Sold), we would implement a "Cheap-Pass" filter using a smaller model (e.g., GPT-4o-mini) for image quality triage, only escalating to high-reasoning models for complex policy edge cases.

## Design Choice: Native Python vs. LangGraph
I deliberately chose to implement the orchestration in **native Python** rather than using frameworks like LangChain or LangGraph. 

**Why?**
* **Auditability:** It’s much easier to debug a standard Python function than a "black-box" agent trace when a customer asks why their claim was rejected.
* **Deterministic Safety:** Warranty claims are a legal and safety process. I wanted a linear state machine that is 100% predictable. Agentic loops can sometimes "reason" their way around a safety gate; native code can't.
* **Speed:** This keeps the Docker image light and the setup simple. 
* **Roadmap:** If the conversation flow gets significantly more complex in the future, we can easily wrap this logic into a LangGraph node.
