from flask import Blueprint, jsonify, current_app

time_bp = Blueprint('time', __name__)

@time_bp.route("/api/time")
def get_time():
    try:
        data = current_app.time_service.get_current_time()
    except Exception:
        # Return a graceful error JSON rather than raising an internal exception
        return jsonify({"error": "Unable to fetch time from TimeService."})
    return jsonify(data)