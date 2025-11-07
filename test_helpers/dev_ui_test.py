# test_helpers/dev_ui_test.py
# 🔍 For manual template testing only

# You can now:
# Test template changes without running the full application
# See how the time view integrates with the overall UI
# Verify navigation and styling work correctly
# Iterate quickly on template designs

import os
from flask import Flask, render_template, Blueprint, redirect

# Configure Flask to find templates in the app/templates directory
app = Flask(__name__, template_folder='../app/templates', static_folder='../app/static')

# Create a blueprint that matches what the template expects
ui_time = Blueprint('ui_time', __name__)

@ui_time.route("/time")
def show_time():
    # Dummy data for testing the Jinja2 template
    print("🎯 DEBUG: /time route hit in dev_ui_test.py")
    return render_template("time_view.html", time_data={
        "utc_datetime": "2025-08-06T17:40:00.000Z [MOCK DATA]",
        "source": "MockTimeService (Development Testing)"
    })

# Register the blueprint
app.register_blueprint(ui_time)

@app.route("/")
def home():
    return redirect("/tasks")

@app.route("/tasks")
def show_tasks():
    return """
    <html>
    <head><title>Tasks</title></head>
    <body>
        <h1>Task List (Mock)</h1>
        <p>This would be your task list page.</p>
        <a href="/time">Go to Time</a>
    </body>
    </html>
    """

@app.route("/tasks/new")
def add_task():
    return """
    <html>
    <head><title>Add Task</title></head>
    <body>
        <h1>Add Task (Mock)</h1>
        <p>This would be your add task form.</p>
        <a href="/tasks">Back to Task List</a> | 
        <a href="/time">Go to Time</a>
    </body>
    </html>
    """

@app.route("/tasks/report")
def task_report():
    return """
    <html>
    <head><title>Task Report</title></head>
    <body>
        <h1>Task Report (Mock)</h1>
        <p>This would be your task analytics/report page.</p>
        <a href="/tasks">Back to Task List</a> | 
        <a href="/time">Go to Time</a>
    </body>
    </html>
    """

@app.route("/time-simple")
def show_time_simple():
    # Simple HTML response without template
    return """
    <html>
    <head><title>Time Test</title></head>
    <body>
        <h1>Simple Time Test</h1>
        <p><strong>UTC Time:</strong> 2025-08-06T17:40:00.000Z [MOCK DATA]</p>
        <p><strong>Source:</strong> MockTimeService (Development Testing)</p>
        <p>This is a simple test without templates.</p>
    </body>
    </html>
    """

@app.route("/debug")
def debug():
    return {
        "routes": [str(rule) for rule in app.url_map.iter_rules()],
        "template_folder": app.template_folder,
        "static_folder": app.static_folder
    }

if __name__ == "__main__":
    app.run(debug=True)