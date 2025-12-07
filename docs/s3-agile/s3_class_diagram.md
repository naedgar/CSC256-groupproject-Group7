
# Sprint 3 Class Diagram

```mermaid
classDiagram
    class TaskService {
        +__init__(repository: TaskRepository)
        +get_all_tasks() List[dict]
        +add_task(title: str) dict
        +complete_task(task_id: int) dict
        +delete_task(task_id: int) None
    }

    class TaskRepository {
        <<interface>>
        +load_tasks() List[dict]
        +save_tasks(tasks: List[dict]) None
    }

    class FileTaskRepository {
        -file_path: str
        +load_tasks() List[dict]
        +save_tasks(tasks: List[dict]) None
    }

    class FlaskAppFactory {
        +create_app() Flask
    }

    class CLI {
        +main_menu()
        +add_task()
        +complete_task()
        +delete_task()
    }

    TaskService --> TaskRepository
    FileTaskRepository ..|> TaskRepository
    FlaskAppFactory --> TaskService
    CLI --> TaskService
