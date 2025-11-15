"""
connector.py — Database Engine + Table Creation
===============================================
Handles:
- SQLAlchemy connection engine (MySQL / fallback SQLite)
- Automatic table creation (trends + memory_log)
- Session management via get_db() dependency
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from loguru import logger
import os

# ---------------------------------------------------------
# 1️⃣ Load Environment Variables
# ---------------------------------------------------------
load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "mysql")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "trend_tracker_db")

# ---------------------------------------------------------
# 2️⃣ Build Database URL (MySQL → fallback SQLite)
# ---------------------------------------------------------
if DB_TYPE == "mysql":
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    DATABASE_URL = "sqlite:///./trend_tracker.db"

# ---------------------------------------------------------
# 3️⃣ Create Engine + Session
# ---------------------------------------------------------
try:
    engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info(f"✅ Database engine connected: {DATABASE_URL}")
except Exception as e:
    logger.error(f"❌ Database connection failed: {e}")
    raise

# ---------------------------------------------------------
# 4️⃣ Function: get_db() Dependency
# ---------------------------------------------------------
def get_db():
    """Yields a new SQLAlchemy session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------------------------------------
# 5️⃣ Function: Initialize Database + Tables
# ---------------------------------------------------------
def init_db():
    """Create required tables if they do not exist."""
    with engine.connect() as connection:
        try:
            logger.info("🧱 Checking and creating necessary tables...")

            # Table: trends
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS trends (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    keyword VARCHAR(255),
                    sentiment_score FLOAT,
                    emotion VARCHAR(50),
                    trend_label VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))

            # Table: memory_log
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS memory_log (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    query TEXT,
                    response_summary TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))

            connection.commit()
            logger.info("✅ Tables verified/created successfully.")

        except Exception as e:
            logger.error(f"❌ Table initialization failed: {e}")
            raise

# ---------------------------------------------------------
# 6️⃣ Auto-Initialize on Import (Optional)
# ---------------------------------------------------------
if __name__ == "__main__":
    init_db()