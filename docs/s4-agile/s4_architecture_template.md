# S4 Architecture 

# 🏗️ Sprint 4 Architecture – Final Group Project

This document describes the **final system architecture** for the TaskTracker Group Project in **Sprint 4 (Final Sprint)**. It supports the following required Group Project user stories and PRs:

- **US031:** Show Current Time via External API  
- **US039:** View Time Created in Task Summary  
- **US0XX:** Hybrid Test Organization with pytest Markers  
- **PR-1 to PR-10:** All final documentation, testing, CI, Robot, and presentation requirements  

---

## 🧩 1. Final Application Architecture (Sprint 4 – Production Flow)

This diagram reflects the **real implementation used in the Group Project**, including:

- Flask App Factory
- API Blueprints
- TaskService & TimeService
- JSON-based persistence
- Centralized validation
- Deprecated CLI

```mermaid
graph TD

%% ========== Entry Point ==========
subgraph EntryPoint
    A[main.py] --> B[create_app]
    A2[cli_app.py (legacy)] -.-> K[Manual CLI Interface - legacy only]
end

%% ========== App Factory ==========
subgraph FlaskAppFactory
    B --> C[Flask App Instance]
    C --> D[Register Blueprint: api/tasks]
    C --> Tz[Register Blueprint: api/time]
    C --> Eh[Register Blueprint: api/health]
    C --> E[Register Error Handlers]
end

%% ========== API Blueprints ==========
subgraph APIBlueprints
    D --> F[routes/api/tasks.py]
    F --> F1[GET /api/tasks]
    F --> F2[POST /api/tasks]
    F --> F3[PUT /api/tasks/id]
    F --> F4[DELETE /api/tasks/id]

    Tz --> Z1[routes/api/time.py]
    Z1 --> Z2[GET /api/time]

    Eh --> H1[routes/api/health.py]
    H1 --> H2[GET /api/health]
end

%% ========== Service Layer ==========
F1 & F2 & F3 & F4 --> S[TaskService app/services/task_service.py]
Z2 --> TS[TimeService app/services/time_service.py]

S --> R[TaskRepository / storage.py (JSON persistence)]

%% ========== Storage Layer ==========
R --> FILE[(data/tasks.json)]

%% ========== Error Handling ==========
E --> J[Global JSON Error Handler]
J --> J1[Handles 400, 404, etc.]

%% ========== Legacy CLI ======
