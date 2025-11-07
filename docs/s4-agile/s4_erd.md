# Sprint 4: Task Tracker ERD

```mermaid
erDiagram
    TASKS {
        int id PK
        string title
        boolean completed
        datetime created_at
        datetime updated_at
    }

    %% === SPRINT 5 EXTENSION CANDIDATES (Optional) ===
    USERS {
        int id PK
        string username
        string email
    }

    TAGS {
        int id PK
        string name
    }

    TASK_TAGS {
        int task_id FK
        int tag_id FK
    }

    %% TAGS and USERS are for future group project features 
    TASKS ||--|| USERS : assigned_to
    TASKS ||--o{ TASK_TAGS : has
    TAGS ||--o{ TASK_TAGS : tagged

```

> 🧠 Sprint 4 ERD (Entity Relationship Diagram)
>
> This diagram reflects the database schema implemented using SQLAlchemy during Sprint 4. The in-memory JSON storage has been replaced with a relational database.
>
> Fields:
>
> * `id`: Primary key, auto-incremented
> * `title`: Required task title (string)
> * `completed`: Boolean flag for task status
> * `created_at`: Timestamp for when the task was created
> * `updated_at`: Timestamp for last modification
>
> 📌 Additional entities (e.g., `tags`, `users`) may be introduced in future sprints. This ERD is aligned with the SQLAlchemy model and supports testability and CRUD operations via ORM.
>
> 🔁 This schema replaces the file-based design from Sprint 3 and is persisted via SQLite or PostgreSQL.
