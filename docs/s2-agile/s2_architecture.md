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
>[!NOTE] In Sprint 1, a basic CLI UI (`cli_app.py`) is introduced to simulate manual task interaction. It allows adding and viewing tasks via terminal input. This CLI is connected to the same in-memory task list as the Flask API and is used for early manual testing (US004).

> [!TIP]
> This CLI interface is intentionally simple in Sprint 1. It supports only adding and viewing tasks and shares the in-memory store with the API. In Sprint 2, the CLI will be extended slightly to reflect new features (US005 – Delete, US006 – Mark Complete) but will remain procedural. Full CLI feature parity is deferred to the Web UI in Sprint 4.


# Sprint 2
```mermaid
graph TD
  subgraph EntryPoint
    A[main.py] --> B[create_app]
    A2[cli_app.py] --> K[Manual CLI Interface]
  end

  subgraph FlaskAppFactory
    B --> C[Flask App Instance]
    C --> D[Register Blueprint: tasks_bp]
    C --> E[Register Error Handlers]
  end

  subgraph Blueprints
    D --> F[routes/tasks.py]
    F --> F1[GET /api/tasks]
    F --> F2[POST /api/tasks]
    F --> F3[PUT /api/tasks/id]
    F --> F4[DELETE /api/tasks/id]
    D --> Fh[routes/health.py]
    Fh --> Fh1[GET /api/health]
  end

  subgraph PersistenceLayer
    F1 --> G1[load_tasks - storage.py]
    F2 --> G2[save_tasks - storage.py]
    F3 --> G2
    F4 --> G2
    G1 --> H[data/tasks.json]
    G2 --> H
    K --> G1
    K --> G2
  end

  subgraph ErrorHandling
    E --> I[Global JSON Error Handler]
    I --> J[Handles 400, 404, etc.]
  end
```

