# S5 Class Diagram

```mermaid
classDiagram

%% ─────────────────────
%% LAYER: Service Layer
%% ─────────────────────

class TaskService {
    +__init__(repository: TaskRepository)
    +get_all_tasks() List[dict]
    +add_task(title: str, description: str) dict
    +complete_task(task_id: int) dict
    +delete_task(task_id: int) None
}

class TimeService {
    +get_current_time() dict
}

class MockTimeService {
    +get_current_time() dict
}

MockTimeService ..|> TimeService

%% ─────────────────────
%% LAYER: Repository Layer
%% ─────────────────────

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

TaskService --> TaskRepository
FileTaskRepository ..|> TaskRepository
DatabaseTaskRepository ..|> TaskRepository

%% ─────────────────────
%% LAYER: Presentation Layer (Routes + App)
%% ─────────────────────

class TaskAPIRoutes {
    +register_routes(bp: Blueprint)
}

class TimeAPIRoutes {
    +register_routes(bp: Blueprint)
}

class TaskUIRoutes {
    +register_routes(bp: Blueprint)
}

class FlaskAppFactory {
    +create_app() Flask
}

FlaskAppFactory --> TaskService
FlaskAppFactory --> TimeService
FlaskAppFactory --> TaskAPIRoutes
FlaskAppFactory --> TimeAPIRoutes
FlaskAppFactory --> TaskUIRoutes

TimeAPIRoutes --> TimeService
```

## 🧩 **Sprint 4 Architectural Highlights**:

- The system now uses `DatabaseTaskRepository` with SQLAlchemy for persistence.
- `TaskService` is injected with a `TaskRepository` using **constructor-based DI** via the app factory.
- `TaskUIRoutes` provides form-based task creation with real-time validation.
- The CLI is now deprecated and fully replaced by the web UI.

---

## 🧩 **Sprint 5 Architectural Highlights**:

* The system now integrates `TimeService` for external API access to [World Time API](http://worldtimeapi.org), with support for mock injection during testing.
* `TimeAPIRoutes` is introduced as a new Flask Blueprint to register the `/api/time` endpoint, using dependency injection.
* `MockTimeService` is used in unit, integration, and Robot Framework acceptance tests to isolate time logic and ensure predictable outputs.
* All service classes (`TaskService`, `TimeService`) are injected via `FlaskAppFactory`, maintaining a clean separation of concerns.
* The architecture now supports **multi-service injection**, laying groundwork for extensibility (e.g., notifications, scheduling).
* Regression and CI testing is expanded to include time-based logic, automated via `pytest`, `requests`, and `Robot Framework`.

---