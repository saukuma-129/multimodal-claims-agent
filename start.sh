#!/bin/sh
set -e

# Seed the ChromaDB vector store only when it is empty.
# Uses upsert so re-running is safe, but this check avoids
# wasting OpenAI embedding API calls on every container restart.
python - <<'EOF'
from app.knowledge.store import PolicyStore
store = PolicyStore()
count = store.collection.count()
if count == 0:
    print("Vector store empty — indexing policy documents...")
    from app.knowledge.ingest import run_ingestion
    run_ingestion()
else:
    print(f"Vector store ready ({count} segments already indexed).")
EOF

# Cloud Run sets $PORT at runtime (default 8080).
# exec replaces the shell process so signals are forwarded correctly.
exec uvicorn app.server:app --host 0.0.0.0 --port "${PORT:-8080}"
