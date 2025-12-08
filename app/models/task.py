class Task:
    """Domain model for a Task, with id, title, description, completed status, and creation timestamp."""
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False, created_at: str = None) -> None:
        self.id: int = task_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = completed
        self.created_at: str = created_at

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def to_dict(self) -> dict[str, object]:
        """Serialize Task object to a dictionary (for JSON serialization)."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }