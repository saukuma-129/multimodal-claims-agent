# ChargePoint AI Claims Agent

Automated warranty claim processing using Multimodal RAG.

## Quick Start
1. Create a `.env` file with your `OPENAI_API_KEY`.
2. Run:
```bash
docker-compose up --build
```
3. **Test the API**:
   - Interactive Docs: Open `http://localhost:8000/docs` to test via the Swagger UI.
   - Direct API: POST a claim to `http://localhost:8000/claims/evaluate` with an image and a description.

## Project Structure
- `app/`: FastAPI logic, Multimodal Analyzer, and Workflow orchestration.
- `engine/`: Deterministic Decision Engine and Priority Logic.
- `data/`: VoltEdge Policy Markdown and sample test images.
- `ARCHITECTURE.md`: Technical deep-dive on scaling and hybrid design.
- `EVALS.md`: "LLM-as-a-Judge" framework and grounding metrics.
- `AI_USAGE.md`: Documentation of architectural overrides and safety gates.
- `README.md`: Setup instructions and project signature.

## 👤 Author
**Saurabh Kumar**
*Staff AI Engineer*
https://www.linkedin.com/in/saurabh-k-38422a103/