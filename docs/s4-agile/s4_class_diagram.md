# S4 Class Diagram

```mermaid
classDiagram
    class TaskService {
        +__init__(self, repository: TaskRepository)
        +get_all_tasks() List[dict]
        +add_task(title: str, description: str) dict
        +complete_task(task_id: int) dict
        +delete_task(task_id: int) None
    }

    class TaskRepository {
        <<interface>>
        +get_all_tasks() List[dict]
        +add_task(title: str, description: str) dict
        +complete_task(task_id: int) dict
        +delete_task(task_id: int) None
    }

    class FileTaskRepository {
        -file_path: str
        +__init__(file_path: str)
        +get_all_tasks() List[dict]
        +add_task(title: str, description: str) dict
        +complete_task(task_id: int) dict
        +delete_task(task_id: int) None
    }

    class DatabaseTaskRepository {
        -db_session
        +__init__(db_session)
        +get_all_tasks() List[dict]
        +add_task(title: str, description: str) dict
        +complete_task(task_id: int) dict
        +delete_task(task_id: int) None
    }

    class TaskAPIRoutes {
        +register_routes(bp: Blueprint)
    }

    class TaskUIRoutes {
        +register_routes(bp: Blueprint)
    }

    class FlaskAppFactory {
        +create_app() Flask
    }

    TaskService --> TaskRepository
    FileTaskRepository ..|> TaskRepository
    DatabaseTaskRepository ..|> TaskRepository
    FlaskAppFactory --> TaskService
    FlaskAppFactory --> TaskAPIRoutes
    FlaskAppFactory --> TaskUIRoutes

```

> 🧩 **Sprint 4 Architectural Highlights**:
>
> - The system now uses `DatabaseTaskRepository` with SQLAlchemy for persistence.
> - `TaskService` is injected with a `TaskRepository` using **constructor-based DI** via the app factory.
> - `TaskUIRoutes` provides form-based task creation with real-time validation.
> - The CLI is now deprecated and fully replaced by the web UI.

