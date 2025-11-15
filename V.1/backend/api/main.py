"""
main.py — FastAPI Core Application
==================================
Handles:
    - API initialization
    - CORS setup
    - Route registration
    - DB initialization
    - Global exception logging
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from dotenv import load_dotenv
import time

# Import routers
from .routes import ingest, analyze, memory, visualize

# DB initialization
from .db.connector import init_db

# Load environment variables
load_dotenv()


# ---------------------------------------------------------
# Create FastAPI app
# ---------------------------------------------------------
app = FastAPI(
    title="Trend Tracker API",
    description="Real-Time Sentiment, Emotion & Trend Analysis Engine",
    version="1.0.0"
)


# ---------------------------------------------------------
# Allow CORS for frontend (React)
# ---------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# API STARTUP EVENT
# ---------------------------------------------------------
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Starting Trend Tracker backend...")
    init_db()
    logger.info("🧱 Database initialized successfully.")


# ---------------------------------------------------------
# API SHUTDOWN EVENT
# ---------------------------------------------------------
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Stopping Trend Tracker backend...")


# ---------------------------------------------------------
# Middleware → Log each request/response
# ---------------------------------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    logger.info(f"➡️ Request: {request.method} {request.url}")
    
    response = await call_next(request)

    duration = time.time() - start_time
    logger.info(f"⬅️ Response: {request.method} {request.url} completed in {duration:.3f}s")

    return response


# ---------------------------------------------------------
# Mount Routers (Corrected to match frontend)
# ---------------------------------------------------------
app.include_router(ingest.router, prefix="/api/ingest")
app.include_router(analyze.router, prefix="/api/analyze")
app.include_router(memory.router, prefix="/api/memory")
app.include_router(visualize.router, prefix="/api/visualize")


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Trend Tracker API is live 🚀",
        "endpoints": [
            "/api/ingest/*",
            "/api/analyze/*",
            "/api/memory/*",
            "/api/visualize/*"
        ]
    }
