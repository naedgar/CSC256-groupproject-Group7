# Class Diagram – Sprint 1

This diagram shows how the main parts of the project work together for Sprint 1.  
Sprint 1 includes only the baseline task functionality migrated from the Individual Project.

```mermaid
classDiagram
    class main {
        +create_app()
    }

    class TaskService {
        +add_task(title, description)
        +get_tasks()
    }

    class InMemoryStore {
        +tasks : list
    }

    class CLIApp {
        +menu()
        +add_task()
        +view_tasks()
    }

    main --> TaskService : uses
    TaskService --> InMemoryStore : stores tasks
    CLIApp --> TaskService : calls
