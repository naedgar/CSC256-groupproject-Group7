# app/services/history_service.py
"""
History Service - Track and store HTTP requests and responses
"""

from datetime import datetime
from typing import List, Dict, Any

class HistoryService:
    """Service for tracking HTTP requests and responses."""
    
    def __init__(self, max_entries: int = 100):
        """
        Initialize the history service.
        
        Args:
            max_entries: Maximum number of history entries to keep (FIFO)
        """
        self._history: List[Dict[str, Any]] = []
        self._max_entries = max_entries
    
    def add_request(self, method: str, endpoint: str, status_code: int = None, 
                   response_time: float = None) -> None:
        """
        Add a request to the history.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint: API endpoint or path
            status_code: HTTP response status code
            response_time: Time taken to process request in milliseconds
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "method": method,
            "endpoint": endpoint,
            "status_code": status_code,
            "response_time_ms": response_time
        }
        
        # Add to history
        self._history.append(entry)
        
        # Keep history size manageable (FIFO - remove oldest entries)
        if len(self._history) > self._max_entries:
            self._history.pop(0)
    
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get all tracked requests in reverse order (newest first).
        
        Returns:
            List of request history entries
        """
        return list(reversed(self._history))
    
    def clear_history(self) -> None:
        """Clear all history entries."""
        self._history = []
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about tracked requests.
        
        Returns:
            Dictionary with statistics (total requests, by method, by status, etc.)
        """
        if not self._history:
            return {
                "total_requests": 0,
                "by_method": {},
                "by_status": {},
                "by_endpoint": {}
            }
        
        stats = {
            "total_requests": len(self._history),
            "by_method": {},
            "by_status": {},
            "by_endpoint": {}
        }
        
        for entry in self._history:
            # Count by method
            method = entry["method"]
            stats["by_method"][method] = stats["by_method"].get(method, 0) + 1
            
            # Count by status code
            if entry["status_code"]:
                status = entry["status_code"]
                stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
            
            # Count by endpoint
            endpoint = entry["endpoint"]
            stats["by_endpoint"][endpoint] = stats["by_endpoint"].get(endpoint, 0) + 1
        
        return stats
