from flask import Blueprint, render_template, current_app

"""
🕒 TIME UI ROUTES - WEB INTERFACE FOR TIME DISPLAY:

This blueprint handles UI routes for displaying time information to users.
It complements the API time routes by providing web pages instead of JSON responses.
"""

ui_time_bp = Blueprint('ui_time', __name__)

@ui_time_bp.route("/time")
def show_time():
    """
    Display current UTC time in a web page.
    
    This route fetches time data from the TimeService and displays it
    using the time_view.html template with proper navigation and styling.
    """
    try:
        # Get time data from the service
        time_data = current_app.time_service.get_current_time()
    except Exception as e:
        # Handle API errors gracefully
        time_data = {
            "error": "Unable to fetch time from external API."
        }
    
    return render_template("time_view.html", time_data=time_data)