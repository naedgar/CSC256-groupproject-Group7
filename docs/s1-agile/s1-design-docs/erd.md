# Entity Relationship Diagram (ERD) – Sprint 1

This diagram shows the main data used by the Task Tracker project.  
In Sprint 1, the data is stored in memory or a JSON file, not a real database yet.  
Later, this will be turned into tables when the team adds a database (like SQLite).

```mermaid
erDiagram
    TASK {
        int id PK
        string title
        string description
        boolean completed
    }

    TIME {
        int id PK
        datetime current_time
        string timezone
    }
