import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI

from .api.routes import router as claims_router

app = FastAPI(
    title="ChargePoint Claims Agent"
)

app.include_router(claims_router)