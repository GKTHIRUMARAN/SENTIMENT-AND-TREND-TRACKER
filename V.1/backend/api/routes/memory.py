"""
memory.py — Memory Storage & Semantic Recall
============================================
Handles:
    - Storing query + summary (JSON memory)
    - Storing embedding vectors (Chroma DB)
    - Retrieving memory entries
    - Clearing memory
"""

from fastapi import APIRouter, HTTPException
from datetime import datetime
import json
import os
from loguru import logger
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------
# Router (NO PREFIX HERE — main.py adds /api/memory)
# ---------------------------------------------------------
router = APIRouter(tags=["Memory"])

# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()
MEMORY_FILE = os.getenv("MEMORY_STORE_PATH", "memory/memory_store.json")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "memory/vector_db/")
MEMORY_RECALL_LIMIT = int(os.getenv("MEMORY_RECALL_LIMIT", 10))

os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
os.makedirs(VECTOR_DB_PATH, exist_ok=True)

# ---------------------------------------------------------
# Load Embedding Model
# ---------------------------------------------------------
logger.info("🔄 Loading embedding model for memory recall...")
try:
    embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    logger.info("✅ Embedding model loaded.")
except Exception as e:
    logger.error(f"❌ Failed to load embedding model: {e}")
    raise

# ---------------------------------------------------------
# Setup ChromaDB
# ---------------------------------------------------------
client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

collection = client.get_or_create_collection(
    name="trend_memory",
    metadata={"hnsw:space": "cosine"}  # distance metric
)

# ---------------------------------------------------------
# Helper: Save a memory entry to JSON
# ---------------------------------------------------------
def _save_memory(entry):
    memory = []

    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                memory = json.load(f)
        except:
            memory = []

    memory.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

    logger.info("🧠 Memory entry saved to memory_store.json")

# ---------------------------------------------------------
# Helper: Save vector embedding
# ---------------------------------------------------------
def _insert_embedding(query_text, summary_text, entry_id):
    sentence = f"{query_text} | {summary_text}"
    embedding = embed_model.encode(sentence).tolist()

    collection.add(
        ids=[entry_id],
        embeddings=[embedding],
        metadatas=[{"query": query_text, "summary": summary_text}],
        documents=[sentence]
    )

    logger.info("📌 Vector embedding saved in Chroma.")

# ---------------------------------------------------------
# Internal ETL Function
# ---------------------------------------------------------
def add_memory_entry(query: str, summary: str):
    """
    Internal ETL pipeline function.
    """
    try:
        entry_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

        entry = {
            "id": entry_id,
            "query": query,
            "summary": summary,
            "timestamp": datetime.now().isoformat()
        }

        _save_memory(entry)
        _insert_embedding(query, summary, entry["id"])

        logger.info("🧠 Memory stored successfully.")
        return entry_id

    except Exception as e:
        logger.error(f"❌ add_memory_entry() failed: {e}")
        raise

# ---------------------------------------------------------
# API 1 — Add Memory Entry
# POST /api/memory/add
# ---------------------------------------------------------
@router.post("/add")
def api_add_memory(query: str, summary: str):
    try:
        entry_id = add_memory_entry(query, summary)
        return {"status": "success", "id": entry_id}

    except Exception as e:
        logger.error(f"❌ /api/memory/add failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------------------------------------
# API 2 — Get All Logs
# GET /api/memory/logs
# ---------------------------------------------------------
@router.get("/logs")
def api_get_logs(limit: int = MEMORY_RECALL_LIMIT):
    try:
        if not os.path.exists(MEMORY_FILE):
            return []

        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

        # Most recent first
        return list(reversed(memory[-limit:]))

    except Exception as e:
        logger.error(f"❌ /api/memory/logs failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------------------------------------
# API 3 — Clear Memory Logs
# POST /api/memory/clear
# ---------------------------------------------------------
@router.post("/clear")
def api_clear_memory():
    try:
        open(MEMORY_FILE, "w").write("[]")
        client.delete_collection("trend_memory")
        client.create_collection(name="trend_memory", metadata={"hnsw:space": "cosine"})

        logger.info("🗑 Memory cleared successfully.")
        return {"status": "cleared"}

    except Exception as e:
        logger.error(f"❌ /api/memory/clear failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
