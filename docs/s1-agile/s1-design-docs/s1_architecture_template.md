# Architecture Diagram

## Sprint 1 – Group Project (Refactored Flask App)
```mermaid
graph TD
  A[main.py] --> B[Flask App Instance]
  B --> C[GET /api/health]
  B --> D[GET /api/tasks]
  B --> E[POST /api/tasks]
  B --> F[PUT /api/tasks/<id>]
  B --> G[DELETE /api/tasks/<id>]
  B --> H[GET /api/time]
  
  CLI[cli_app.py] --> I[Menu: Add/View Tasks]
  
  C --> J[TaskService]
  D --> J
  E --> J
  F --> J
  G --> J
  H --> K[TimeService]
  
  J --> L[Pydantic Validation]
  J --> M[JSON / SQLite Storage]
  I --> J

  subgraph Testing
    T1[pytest]
    T2[Robot Framework]
  end

  Testing --> B
  Testing --> J
