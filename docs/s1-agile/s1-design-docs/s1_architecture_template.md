# Architecture Diagram

## Sprint 1 Monolithic
```mermaid
graph TD
  A[main.py] --> B[Flask App Instance]
  B --> C[GET /api/health]
  B --> D[GET /api/tasks]
  B --> E[POST /api/tasks]
  B --> F[PUT /api/tasks/id]
  B --> G[DELETE /api/tasks/id]
  
  CLI[cli_app.py] --> H[Menu: Add/View Tasks]
  
  C --> I[In-Memory Task List]
  D --> I
  E --> I
  F --> I
  G --> I
  H --> I
```
> [!TIP]
> This CLI interface is intentionally simple in Sprint 1. It supports only adding and viewing tasks and shares the in-memory store with the API. In Sprint 2, the CLI will be extended slightly to reflect new features (US005 – Delete, US006 – Mark Complete) but will remain procedural. Full CLI feature parity is deferred to the Web UI in Sprint 4.

