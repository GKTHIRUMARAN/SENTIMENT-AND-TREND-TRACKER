/* ============================================================
   📘 Trend Tracker — Database Query Definitions
   File: backend/api/db/queries.sql
   Purpose:
     - Define reusable SQL statements for all CRUD operations
     - Support analysis, logging, and visualization layers
   ============================================================ */

-- ============================================================
-- 🧱 TABLE CREATION (Safety)
-- ============================================================
CREATE TABLE IF NOT EXISTS trends (
    id INT AUTO_INCREMENT PRIMARY KEY,
    keyword VARCHAR(255) NOT NULL,
    sentiment_score FLOAT,
    emotion VARCHAR(50),
    trend_label VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS memory_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query TEXT,
    response_summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- ➕ INSERT QUERIES
-- ============================================================
-- Insert a new record into trends
INSERT INTO trends (keyword, sentiment_score, emotion, trend_label)
VALUES (:keyword, :sentiment_score, :emotion, :trend_label);

-- Insert memory log (query + summary)
INSERT INTO memory_log (query, response_summary)
VALUES (:query, :response_summary);

-- ============================================================
-- 🔍 READ / SELECT QUERIES
-- ============================================================
-- Fetch all trend entries
SELECT * FROM trends ORDER BY created_at DESC;

-- Fetch latest N trend entries
SELECT * FROM trends ORDER BY created_at DESC LIMIT :limit;

-- Fetch trend records by keyword
SELECT * FROM trends WHERE keyword = :keyword ORDER BY created_at DESC;

-- Aggregate average sentiment per keyword
SELECT keyword, AVG(sentiment_score) AS avg_sentiment
FROM trends
GROUP BY keyword
ORDER BY avg_sentiment DESC;

-- Count emotion distribution
SELECT emotion, COUNT(*) AS count
FROM trends
GROUP BY emotion
ORDER BY count DESC;

-- Retrieve recent memory logs
SELECT * FROM memory_log ORDER BY created_at DESC LIMIT :limit;

-- ============================================================
-- ✏️ UPDATE QUERIES
-- ============================================================
-- Update trend label or sentiment by ID
UPDATE trends
SET trend_label = :trend_label,
    sentiment_score = :sentiment_score
WHERE id = :id;

-- ============================================================
-- ❌ DELETE QUERIES
-- ============================================================
-- Delete specific trend record
DELETE FROM trends WHERE id = :id;

-- Delete memory logs older than X days
DELETE FROM memory_log
WHERE created_at < NOW() - INTERVAL :days DAY;

-- ============================================================
-- 📊 ANALYTICS / VISUALIZATION HELPERS
-- ============================================================
-- Daily trend count
SELECT DATE(created_at) AS date, COUNT(*) AS total
FROM trends
GROUP BY DATE(created_at)
ORDER BY date DESC;

-- Keyword frequency ranking
SELECT keyword, COUNT(*) AS frequency
FROM trends
GROUP BY keyword
ORDER BY frequency DESC
LIMIT 10;

-- Sentiment summary counts
SELECT
  SUM(CASE WHEN sentiment_score > 0.05 THEN 1 ELSE 0 END) AS positive,
  SUM(CASE WHEN sentiment_score BETWEEN -0.05 AND 0.05 THEN 1 ELSE 0 END) AS neutral,
  SUM(CASE WHEN sentiment_score < -0.05 THEN 1 ELSE 0 END) AS negative
FROM trends;

-- ============================================================
-- ✅ END OF FILE
-- ============================================================