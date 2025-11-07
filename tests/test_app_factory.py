# tests/test_app_factory.py
from app import create_app
from flask import Flask

"""
📚 STUDENT NOTE: Why was test_app_returns_404_when_no_routes_defined updated?

🔍 WHAT HAPPENED:
The test `test_app_returns_404_when_no_routes_defined` was failing because it expected 
a 404 status code when accessing the home route ("/"), but was getting a 302 (redirect) instead.

🤔 WHY DID THIS HAPPEN:
Originally, the application had NO route defined for "/" (the home page), so accessing 
it would return a 404 "Not Found" error. However, we improved the user experience by 
adding a home route that redirects users to the task creation form.

⚡ THE CHANGE:
We changed the test to check for a 302 (redirect) status code instead of a 404.
This change means that now, when users access the home page ("/"), they are redirected 
to the task creation form ("/tasks/new") instead of receiving a 404 error.

🧪 TEST EVOLUTION:
When application behavior changes, tests must be updated to match 
the new expected behavior. The old test was checking for behavior that no longer exists.

📖 LESSON LEARNED:
- Tests should reflect CURRENT application behavior, not outdated behavior
- When you improve UX (like adding a helpful redirect), update tests accordingly
- A 302 redirect is often better UX than a 404 error for the home page
- Test names and descriptions should clearly describe what they're actually testing

This is a normal part of software development - as features evolve, tests evolve too!
"""

def test_create_app_returns_flask_instance():
    """
    tc-us000-002: The create_app function should return a Flask app instance.
    """
    app = create_app()
    assert isinstance(app, Flask)

def test_app_returns_redirect_for_home_route():
    """
    tc-us000-003: The Flask app should redirect from home page to task form.
    """
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 302  # Redirect status
    assert '/tasks/new' in response.location

def test_app_uses_db_repo():
    """
    TC-RF011-001: Flask App Loads with DB Injection
    Verifies that create_app() properly wires database repository and service
    """
    app = create_app()
    assert hasattr(app, "task_service")
    
    # Additional verification that it's a proper service
    assert app.task_service is not None
    assert hasattr(app.task_service, 'add_task')
    assert hasattr(app.task_service, 'get_tasks')