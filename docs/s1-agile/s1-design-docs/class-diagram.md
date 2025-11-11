# Class Diagram – Sprint 1

This diagram shows how the main parts of the project work together.  
It helps you see what each file or class does in a simple way.

```mermaid
classDiagram
    class main {
        +create_app()
    }

    class TaskService {
        +add_task(title, description)
        +get_tasks()
    }

    class TimeService {
        +get_current_time()
    }

    class CLIApp {
        +menu()
        +add_task()
        +view_tasks()
    }

    main --> TaskService : uses
    main --> TimeService : uses
    CLIApp --> TaskService : calls