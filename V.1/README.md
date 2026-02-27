# Sentiment & Trend Tracker — V1 Full Implementation

> Modular NLP analytics system with sentiment classification, topic modeling, forecasting, and API-driven dashboard using FastAPI and React.

---

## Overview

V1 expands the V0 prototype into a structured full-stack implementation.

This version integrates:

- FastAPI backend for ingestion and analysis
- Automated ETL pipeline
- Sentiment and emotion classification
- Topic modeling
- Trend forecasting
- Persistent storage and logging
- React-based dashboard

The system is designed with modular separation between ingestion, preprocessing, model execution, and visualization layers.

---

## Architectural Objectives

1. Replace prototype-bound execution with API-based orchestration.
2. Support both manual and CSV ingestion.
3. Integrate multiple NLP models in a unified pipeline.
4. Store analysis results and historical summaries.
5. Serve visualization-ready JSON to frontend.
6. Prepare for real-time ingestion in future versions.

---

## High-Level Architecture

User Input (Text / CSV)  
→ React Dashboard  
→ FastAPI Backend  
→ Ingestion Module  
→ Preprocessing Layer  
→ Model Execution Layer  
→ Results Storage  
→ Visualization API  
→ Frontend Rendering  

Memory and embedding storage are handled independently of the analysis pipeline.

---

## Backend Structure

backend/ ├── api/ │   ├── main.py │   ├── routes/ │   ├── utils/ │   ├── db/ ├── pipeline/ └── .env

Responsibilities:

- Dataset ingestion
- Text preprocessing
- Model orchestration
- Forecast computation
- Memory storage
- Visualization formatting
- Logging

---

## Model Layer

### Sentiment
- VADER polarity scoring

### Emotion
- DistilRoBERTa-based classification

### Topic Modeling
- BERTopic clustering

### Forecasting
- Prophet for short-term trend projection

Each model runs independently and outputs structured intermediate results before aggregation.

---

## Data Flow

1. Ingest raw input.
2. Normalize and preprocess text.
3. Execute sentiment and emotion models.
4. Generate topic clusters.
5. Forecast trends based on aggregated time-series.
6. Persist results.
7. Return structured JSON for dashboard rendering.

---

## Storage Components

- Raw input files
- Cleaned datasets
- Results CSV
- Serialized model artifacts
- Memory JSON store
- Vector embedding storage
- Log files for ETL and API events

Database integration via SQLAlchemy is supported but optional.

---

## Frontend Responsibilities

Built using React.

- Submit text or dataset
- Render KPIs
- Display sentiment distribution
- Display topic clusters
- Render forecast charts
- Access memory history

Frontend contains no business logic; all analytics remain backend-controlled.

---

## Core Endpoints

POST `/api/ingest`
- Accepts text or CSV input

POST `/api/analyze`
- Executes full NLP pipeline

GET `/api/visualize`
- Returns chart-ready JSON

GET `/api/memory`
- Retrieves historical summaries

---

## Engineering Improvements Over V0

- Offline script → API-based orchestration
- Single model → Multi-model integration
- No persistence → Structured storage
- Static dashboard → Reactive frontend
- Manual execution → Automated ETL cycle
- No memory → Historical summary + embeddings

---

## Current Capabilities

- Multi-model NLP analysis
- Topic clustering
- Time-series forecasting
- Automated ETL execution
- Persistent storage
- Memory tracking
- React dashboard integration
- Logging across pipeline

---

## Known Limitations

- No streaming ingestion
- Limited evaluation metrics exposed
- No distributed processing
- No containerized deployment in this version
- Forecast accuracy dependent on dataset quality
- GPU acceleration not implemented

---

## Local Execution

Backend:

```bash
uvicorn backend.api.main:app --reload
```bash
Frontend:
```bash
cd frontend/react_app
npm install
npm run dev

Access:

http://localhost:5173
```bash

---

## Evolution Path

Version	Scope

V0	Offline NLP prototype
V1	Modular API-based multi-model analytics
V2 (Planned)	Real-time ingestion + distributed scaling



---

This project demonstrates:

NLP pipeline integration

Multi-model orchestration

API-first architecture

Frontend-backend separation

Forecasting integration

Memory and embedding handling


It represents the analytics counterpart to the conversational AI and HR analytics systems.


---

Developer

Thirumaran GK
AI Systems & Analytics Engineer
Coimbatore, Tamil Nadu, India
LinkedIn: https://linkedin.com/in/thirumarangk-ai
GitHub: https://github.com/GKTHIRUMARAN