from flask import Blueprint, jsonify, current_app

time_bp = Blueprint('time', __name__)

@time_bp.route("/api/time")
def get_time():
    return jsonify(current_app.time_service.get_current_time())