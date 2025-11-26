from flask import Blueprint, render_template, current_app, request
"""
🕒 TIME UI ROUTES - WEB INTERFACE FOR TIME DISPLAY:

This blueprint handles UI routes for displaying time information to users.
It complements the API time routes by providing web pages instead of JSON responses.
"""

ui_time_bp = Blueprint('ui_time', __name__)

@ui_time_bp.route("/time")
def show_time():
    """
    Display current time in a web page for the selected timezone.
    
    This route fetches time data from the TimeService based on the timezone
    query parameter and displays it using the time_view.html template.
    """
    # Get timezone from query parameter, default to UTC
    selected_timezone = request.args.get('timezone', 'UTC')
    
    try:
        # Get time data from the service with selected timezone
        time_data = current_app.time_service.get_current_time(selected_timezone)
    except Exception as e:
        # Handle API errors gracefully
        time_data = {
            "error": "Unable to fetch time from external API.",
            "timezone": selected_timezone
        }
    
    return render_template("time_view.html", time_data=time_data, selected_timezone=selected_timezone)