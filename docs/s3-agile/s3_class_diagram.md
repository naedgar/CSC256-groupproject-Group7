```mermaid
classDiagram
    class TaskService {
        +__init__(self, repository: TaskRepository)
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
        +__init__(file_path: str)
        +load_tasks() List[dict]
        +save_tasks(tasks: List[dict]) None
    }

    class TaskRoutes {
        +register_routes(bp: Blueprint)
    }

    class FlaskAppFactory {
        +create_app() Flask
    }

    class CLI {
        +main_menu()
    }

    TaskService --> TaskRepository
    FileTaskRepository ..|> TaskRepository
    FlaskAppFactory --> TaskService
    FlaskAppFactory --> TaskRoutes
    CLI --> TaskService
```

> 📌 This class diagram illustrates the separation of concerns using OOP principles in Sprint 3:
>
> * `TaskService` handles logic.
> * `TaskRepository` is an interface for persistence.
> * `FileTaskRepository` implements JSON file storage.
> * `TaskRoutes` holds Blueprint route logic.
> * `FlaskAppFactory` wires everything together.

You may later extend this by adding a `DatabaseTaskRepository` that also implements `TaskRepository` in Sprint 4.



```mermaid
classDiagram
    class TaskService {
        +__init__(self, repository: TaskRepository)
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
        +__init__(file_path: str)
        +load_tasks() List[dict]
        +save_tasks(tasks: List[dict]) None
    }

    class TaskRoutes {
        +register_routes(bp: Blueprint)
    }

    class FlaskAppFactory {
        +create_app() Flask
    }

    class CLI {
        +main_menu()
    }

    TaskService --> TaskRepository
    FileTaskRepository ..|> TaskRepository
    FlaskAppFactory --> TaskService
    FlaskAppFactory --> TaskRoutes
    CLI --> TaskService
```

> 💡 `CLI` is included as a transitional interface. It will be deprecated in Sprint 4 when a Web UI is introduced.
