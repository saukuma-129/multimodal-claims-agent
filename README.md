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
   - Direct API: POST to `http://localhost:8000/claims/evaluate` (or your specific route).

## Project Structure
- `/app`: FastAPI logic and ClaimWorkflow.
- `/engine`: Deterministic rule engine and Priority Queue.
- `/data`: VoltEdge Policy Markdown and vector store.
- `/docs`: Architecture, Evals, and AI Usage logs.

## 👤 Author
**Saurabh Kumar**
*Staff AI Engineer*
https://www.linkedin.com/in/saurabh-k-38422a103/