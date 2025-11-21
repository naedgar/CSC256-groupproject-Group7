"""
app/exceptions.py - Custom Exception Classes

Centralized exception definitions for consistent error handling
across the application (API, UI, and service layers).
"""


class TaskValidationError(Exception):
    """
    Raised when task data fails validation rules.
    
    This exception captures validation errors at the service layer
    and allows both API and UI routes to handle them consistently.
    
    Attributes:
        message: User-friendly error message
        field: Optional field name that caused the error
        details: Optional additional error details (for API responses)
    
    Example:
        >>> raise TaskValidationError("Title cannot be empty", field="title")
    """
    
    def __init__(self, message: str, field: str = None, details: dict = None):
        """
        Initialize the validation error.
        
        Args:
            message: User-facing error message
            field: Optional field name that triggered the error
            details: Optional dict with additional error information
        """
        self.message = message
        self.field = field
        self.details = details or {}
        super().__init__(self.message)
    
    def to_dict(self):
        """Convert error to dictionary for JSON responses."""
        error_dict = {"error": self.message}
        if self.field:
            error_dict["field"] = self.field
        if self.details:
            error_dict.update(self.details)
        return error_dict
