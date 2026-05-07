from fastapi import FastAPI
from app.api.routes import router as claims_router

app = FastAPI(title="ChargePoint Claims Agent")

app.include_router(claims_router)
