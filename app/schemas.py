"""
app/schemas.py - Centralized Task Validation Schemas

This module defines validation schemas for task validation, providing:
- Single source of truth for task validation rules
- Consistent validation across API and UI routes
- Automatic data normalization (trimming, type conversion)
- Clear error messages for invalid input

Business Rules Defined:
✅ Title: Required, 1-255 characters, trimmed automatically
✅ Description: Optional, max 500 characters, trimmed automatically
✅ Reusable across API and UI routes
"""

from typing import Optional
from app.exceptions import TaskValidationError


class TaskCreate:
    """Schema for creating a new task.
    
    Validates and normalizes task input data.
    
    Business Rules:
    - title: Required, max 255 characters, trimmed automatically
    - description: Optional, max 500 characters, trimmed automatically
    
    Example:
        >>> task_data = TaskCreate(title="  Buy milk  ", description="From store")
        >>> task_data.title
        'Buy milk'
        >>> task_data.description
        'From store'
    """
    
    MAX_TITLE_LENGTH = 255
    MAX_DESCRIPTION_LENGTH = 500
    
    def __init__(self, title: str, description: Optional[str] = None):
        """
        Initialize and validate task data.
        
        Args:
            title: Task title (required)
            description: Task description (optional)
            
        Raises:
            TaskValidationError: If validation fails
        """
        # Validate and normalize title
        self.title = self._validate_title(title)
        
        # Validate and normalize description
        self.description = self._validate_description(description)
    
    def _validate_title(self, title: str) -> str:
        """
        Validate and normalize title.
        
        Rules:
        - Required field
        - Must not be empty or whitespace
        - Must not exceed MAX_TITLE_LENGTH
        - Automatically trimmed
        
        Args:
            title: Raw title input
            
        Returns:
            Normalized title
            
        Raises:
            TaskValidationError: If validation fails
        """
        # Check if None (missing)
        if title is None:
            raise TaskValidationError(
                "Title is required",
                field="title"
            )
        
        # Check type
        if not isinstance(title, str):
            raise TaskValidationError(
                "Title must be a string",
                field="title"
            )
        
        # Strip whitespace
        trimmed = title.strip()
        
        # Check required
        if not trimmed:
            raise TaskValidationError(
                "Title is required",
                field="title"
            )
        
        # Check max length
        if len(trimmed) > self.MAX_TITLE_LENGTH:
            raise TaskValidationError(
                f"Title must not exceed {self.MAX_TITLE_LENGTH} characters",
                field="title",
                details={"length": len(trimmed), "max": self.MAX_TITLE_LENGTH}
            )
        
        return trimmed
    
    def _validate_description(self, description: Optional[str]) -> str:
        """
        Validate and normalize description.
        
        Rules:
        - Optional field
        - Must not exceed MAX_DESCRIPTION_LENGTH if provided
        - Automatically trimmed and defaulted to empty string
        
        Args:
            description: Raw description input
            
        Returns:
            Normalized description (empty string if None)
            
        Raises:
            TaskValidationError: If validation fails
        """
        # Default to empty string if None
        if description is None:
            return ""
        
        # Check type
        if not isinstance(description, str):
            raise TaskValidationError(
                "Description must be a string",
                field="description"
            )
        
        # Strip whitespace
        trimmed = description.strip()
        
        # Check max length
        if len(trimmed) > self.MAX_DESCRIPTION_LENGTH:
            raise TaskValidationError(
                f"Description must not exceed {self.MAX_DESCRIPTION_LENGTH} characters",
                field="description",
                details={"length": len(trimmed), "max": self.MAX_DESCRIPTION_LENGTH}
            )
        
        return trimmed
    
    def to_dict(self) -> dict:
        """Convert validated data to dictionary."""
        return {
            "title": self.title,
            "description": self.description
        }
