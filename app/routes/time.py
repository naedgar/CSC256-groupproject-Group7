from flask import Blueprint, jsonify, current_app

time_bp = Blueprint('time', __name__)

@time_bp.route("/api/time")
def get_time():
    """
    Get current time from TimeService.
    
    The TimeService handles most exceptions internally, but we need to catch
    any unexpected errors (like when a test injects a broken service).
    """
    try:
        data = current_app.time_service.get_current_time()
        # If the service returns an error dict, that's still a valid response
        return jsonify(data)
    except Exception as e:
        # Only catches truly unexpected exceptions (e.g., from test mocking)
        # Return a graceful fallback response
        return jsonify({
            "error": "Unable to fetch time from TimeService.",
            "details": str(e) if current_app.config.get('TESTING') else None
        })