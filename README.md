# Task Tracker Application - Group Project Sprint 2

A comprehensive Flask-based task management application demonstrating modern software engineering practices, including Test-Driven Development (TDD), Behavior-Driven Development (BDD), and comprehensive automated testing.

## 🎯 Project Overview

This is a learning project that demonstrates:
- **Flask Web Application** - Full-stack task management system
- **Test-Driven Development (TDD)** - Unit, integration, and API testing
- **Behavior-Driven Development (BDD)** - Acceptance testing with pytest-bdd + Playwright
- **Multiple UI Testing Frameworks** - Selenium and Playwright comparison
- **CI/CD Pipeline** - GitHub Actions with comprehensive test automation
- **Database Integration** - SQLAlchemy with SQLite
- **Professional Code Structure** - Application factory pattern, dependency injection

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ (recommended: 3.13.5)
- Virtual environment (required)

### Setup

1. **Clone and navigate to your project:**
   ```bash
   cd your-repo-directory
   ```

2. **Create and activate virtual environment:**
   ```powershell
   # PowerShell (Windows)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   
   ```bash
   # Git Bash / Linux / macOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers (for UI testing):**
   ```bash
   playwright install chromium
   ```

5. **Run the application:**
   ```bash
   python -m app.main
   ```

6. **Access the application:**
   - Web Interface: http://localhost:5000
   - API Health Check: http://localhost:5000/api/health

## 🧪 Testing Strategy

This project demonstrates comprehensive testing at multiple levels with **proper test separation**:

### Test Separation Overview

The project uses **industry standard test separation** to prevent conflicts:

- **Main Test Suite (80+ tests)**: Unit, integration, API, and UI tests using sync fixtures
- **BDD Acceptance Tests**: Separate test suite using async pytest-playwright fixtures
- **pytest.ini Configuration**: Excludes BDD tests from main runs to prevent asyncio conflicts

### Running Tests

#### Main Test Suite (Recommended for Daily Development)
```bash
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate    # Linux/macOS

# Run all main tests (excludes BDD tests via pytest.ini)
pytest -v

# Run specific test categories
pytest tests/api/ -v                    # API tests only
pytest tests/ui/selenium/ -v            # Selenium UI tests
pytest tests/ui/playwright/ -v          # Playwright UI tests (custom fixtures)
pytest tests/storage/ -v                # Database tests
```

#### BDD Acceptance Tests (Separate Test Suite)
```bash
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate    # Linux/macOS

# Start Flask server in separate terminal
python -m app.main

# Run BDD tests separately (requires pytest-playwright)
pytest tests/acceptance/bdd_playwright/ -v

# BDD tests with advanced features
pytest tests/acceptance/bdd_playwright/ --headed --browser=firefox -v
pytest tests/acceptance/bdd_playwright/ --html=results/bdd_report.html --self-contained-html -v
```

#### Coverage Report
```bash
# Generate coverage report (main test suite)
pytest --cov=app --cov-report=html --cov-report=term-missing
```

### Why Test Separation?

- ✅ **Prevents Conflicts**: Avoids asyncio issues between sync and async test fixtures
- ✅ **Optimizes Performance**: Main test suite runs fast (80+ tests in ~30 seconds)
- ✅ **Professional Practice**: Different test types serve different purposes
- ✅ **Clear Boundaries**: Unit/integration tests vs. end-to-end acceptance tests

### Hybrid Test Organization (PR-3)

This repository uses a hybrid test organization: tests are grouped by concern (folder structure) and by scope using pytest markers. That makes tests easy to find and quick to run by scope.

- Folder structure (examples): `tests/api/`, `tests/storage/`, `tests/ui/playwright/`, `tests/ui/selenium/`, `tests/time/`.
- Pytest markers: `unit`, `integration`, `e2e` (registered in `pytest.ini`).

Add the following to `pytest.ini` (already present in this project) to register markers:

```ini
[pytest]
markers =
   unit: fast, isolated function/class tests
   integration: database, file, or service interaction tests
   e2e: end-to-end UI/browser tests (Playwright, Selenium, Robot)
```

Run tests by scope (examples):

```bash
# run only unit tests
pytest -m unit

# run only integration tests
pytest -m integration

# run only end-to-end (UI) tests
pytest -m e2e

# run unit OR integration
pytest -m "unit or integration"
```

Documentation and evidence:
- Save text outputs, HTML reports or terminal screenshots in `docs/screenshots/` (e.g., `pytest-unit-output.txt`, `unit-report.html`, `pytest-unit-terminal.png`).
- Reference these artifacts in your Test Plan and PR description.

### PR-4: Automated Testing of Time Service

This project implements PR-4 by adding a focused test suite and CI workflows for the Time Service feature. Summary of changes made:

- **New tests added**: Unit and integration tests and end-to-end UI tests for the Time Service were added under the `tests/time/` and `tests/ui/` directories:
   - `tests/time/test_time_unit_additional.py` — additional unit tests (fallback and format checks).
   - `tests/api/test_time_integration_additional.py` — integration test verifying graceful API behavior on service failure.
   - `tests/ui/playwright/test_time_e2e.py` — Playwright E2E test that verifies the `/time` UI displays UTC time and updates.
   - `tests/ui/selenium/test_time_selenium.py` — Selenium E2E test (headless Chrome) that validates the UI time and update behavior.

- **Service robustness**: The API route handling time was made resilient to service errors:
   - `app/routes/time.py` now catches exceptions from `TimeService` and returns a graceful JSON error (keeps prior behavior of returning JSON so existing clients/tests stay compatible).

- **Dev/test dependencies**:
   - Added `tests/requirements-dev.txt` containing `pytest-playwright`, `playwright`, `selenium`, `webdriver-manager`, and other development-only packages used by the new tests.

- **CI workflows**:
   - Added separate GitHub Actions workflows for Playwright and Selenium:
      - `.github/workflows/playwright-e2e.yml` — installs Playwright browsers and runs Playwright tests in `tests/ui/playwright`.
      - `.github/workflows/selenium-e2e.yml` — runs Selenium E2E tests in `tests/ui/selenium`.
   - Workflows are configured with `paths` filters and `workflow_dispatch` to support automatic runs on relevant changes and manual runs by reviewers.

- **Test fixtures**: Playwright fixtures in `tests/ui/playwright/conftest.py` were used by the new Playwright test to avoid async/sync conflicts and ensure reliable browser setup.

- **How to run Time Service tests locally**:
   1. Install dev dependencies (recommended in an activated virtualenv):

       ```bash
       pip install -r requirements.txt
       pip install -r tests/requirements-dev.txt
       python -m playwright install --with-deps
       ```

   2. Run unit and integration tests:

       ```bash
       pytest -m unit
       pytest -m integration
       ```

   3. Run Playwright E2E (make sure the app server is available — `tests/ui/playwright/conftest.py` performs a health check):

       ```bash
       pytest tests/ui/playwright -m e2e -q
       ```

   4. Run Selenium E2E (uses `webdriver-manager` to install ChromeDriver automatically):

       ```bash
       pytest tests/ui/selenium -m e2e -q
       ```

- **Evidence & artifacts**:
   - Test outputs, HTML coverage, and screen recordings/screenshots (Playwright) should be saved under `test-results/` or `docs/screenshots/` as part of the run pipeline.
   - Example artifacts in this repo after running tests: `htmlcov/` (coverage) and `test-results/videos` / `test-results/screenshots`.

- **Notes**:
   - Playwright tests use custom fixtures to avoid the async/sync loop error. If you see `It looks like you are using Playwright Sync API inside the asyncio loop`, make sure to run Playwright tests in their own collection (`tests/ui/playwright`) and use the provided fixtures.
   - If you see a Selenium `WebDriver.__init__() got multiple values for argument 'options'` error, ensure ChromeDriver is created via `Service(...)` and passed using keyword `options=` as implemented in `tests/ui/selenium/test_time_selenium.py`.

- **Backlog update**: Update `tt_user_stories.md` to mark PR-4 completed and point to these files and CI workflow runs as evidence.

CI behavior (recommended):
- Primary workflow (`.github/workflows/python-app.yml`) runs only `unit` + `integration` tests (this repo runs `pytest -m "unit or integration"` in the coverage step).
- E2E/UI and Robot workflows should be in separate workflow files (e.g. `.github/workflows/e2e-tests.yml`) with path filters, `workflow_dispatch` for manual runs, and an optional PR-label override to force runs when needed.


## 📁 Project Structure

```
your-project/
├── app/                          # Main application package
│   ├── __init__.py              # Application factory
│   ├── main.py                  # Application entry point
│   ├── models/                  # Data models
│   ├── repositories/            # Data access layer
│   ├── services/                # Business logic layer
│   ├── routes/                  # API and UI endpoints
│   ├── templates/               # Jinja2 templates
│   └── static/                  # CSS, JS, images
├── tests/                       # Test suite
│   ├── api/                     # API integration tests
│   ├── ui/                      # UI tests (Selenium, Playwright)
│   │   ├── selenium/            # Selenium-based UI tests
│   │   └── playwright/          # Playwright with custom fixtures
│   ├── acceptance/              # BDD acceptance tests (separate)
│   │   └── bdd_playwright/      # pytest-bdd + pytest-playwright
│   ├── storage/                 # Database tests
│   ├── tasks/                   # Business logic tests
│   └── health/                  # Development environment verification
├── docs/                        # Sprint documentation
│   ├── sprint1/                 # Sprint 1 documentation
│   ├── sprint2/                 # Sprint 2 documentation  
│   ├── sprint3/                 # Sprint 3 documentation
│   ├── sprint4/                 # Sprint 4 documentation
│   └── sprint5/                 # Sprint 5 documentation
│       ├── sprint_plan.md       # Sprint objectives and deliverables
│       ├── api_reference.md     # Current API documentation
│       ├── architecture.md      # System design and patterns
│       ├── class_diagram.md     # UML class diagrams (Mermaid)
│       ├── erd_diagram.md       # Entity relationship diagrams (Mermaid)
│       ├── test_cases.md        # Detailed test specifications  
│       ├── test_plan.md         # Testing strategy and execution
│       └── user_journey.md      # User flow documentation
├── cli/                         # Command-line interface
├── test_helpers/                # Test utilities and helpers
├── labs/                        # Lab instructions and documentation
├── scripts/                     # Automation scripts (optional)
├── results/                     # Test reports and artifacts
├── .github/workflows/           # CI/CD configuration
├── requirements.txt             # Python dependencies
└── pytest.ini                  # pytest configuration with BDD exclusions
```

## 🔧 Technology Stack

### Core Framework
- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **Jinja2** - Template engine

### Testing Frameworks
- **pytest** - Test runner and framework
- **pytest-bdd** - BDD testing with Gherkin scenarios
- **pytest-playwright** - Industry standard Playwright plugin  
- **Playwright** - Modern browser automation
- **Selenium** - Cross-browser testing (educational comparison)
- **pytest-html** - HTML test reports
- **pytest-cov** - Code coverage

### Development Tools
- **Black** - Code formatting
- **Flake8** - Code linting
- **MyPy** - Type checking

## 🎭 BDD Acceptance Testing

This project includes **Behavior-Driven Development (BDD)** testing for end-to-end acceptance scenarios using pytest-bdd and pytest-playwright.

### BDD Overview
- **Purpose**: End-to-end acceptance testing with business-readable scenarios
- **Tools**: pytest-bdd + pytest-playwright (industry standard)
- **Separation**: Runs independently from main test suite to prevent conflicts
- **Features**: Video recording, screenshots, cross-browser testing, rich reporting

### Quick BDD Usage
```bash
# Start Flask server (separate terminal)
python -m app.main

# Run BDD acceptance tests
pytest tests/acceptance/bdd_playwright/ -v
```

📚 **[Complete BDD Setup & Usage Guide →](tests/acceptance/bdd_playwright/README.md)**

## 🚀 CI/CD Pipeline

GitHub Actions workflow includes:
- **Unit Tests** - Fast, isolated component testing
- **Integration Tests** - API endpoint testing  
- **UI Tests** - Selenium and Playwright browser testing
- **BDD Tests** - End-to-end acceptance testing (separate workflow)
- **Code Coverage** - Coverage reporting with artifacts
- **Cross-Platform** - Linux (Ubuntu) testing environment

## 📊 Test Reports

Generated reports include:
- **HTML Coverage Report** - `htmlcov/index.html`
- **Pytest HTML Report** - `results/report.html`  
- **JUnit XML** - `results/junit.xml`
- **BDD Reports** - Rich media reports (see BDD documentation)

## 🛠️ Development Workflow

1. **Create feature branch:**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Write tests first (TDD):**
   ```bash
   # Write failing test
   pytest tests/test_new_feature.py::test_new_functionality -v
   ```

3. **Implement feature:**
   ```bash
   # Implement code to make test pass
   pytest tests/test_new_feature.py::test_new_functionality -v
   ```

4. **Run full test suite:**
   ```bash
   # Main test suite (excludes BDD)
   pytest -v
   
   # BDD tests separately (if relevant to feature)
   pytest tests/acceptance/bdd_playwright/ -v
   ```

5. **Create pull request and wait for CI:**
   - All tests must pass
   - Coverage thresholds must be met

## 🎓 Educational Features

This project demonstrates:
- **Test Pyramid** - Unit → Integration → UI → BDD
- **Test Separation** - Appropriate tools for different test types
- **Clean Architecture** - Separation of concerns
- **Dependency Injection** - Testable design patterns
- **Factory Pattern** - Flask application factory
- **Repository Pattern** - Data access abstraction
- **Service Layer** - Business logic separation
- **Continuous Integration** - Automated testing pipeline

## 🔧 Environment Management

### Virtual Environment Best Practices

**Critical for Complex Testing:**
The virtual environment becomes increasingly important as you add testing frameworks:

```bash
# Always activate before any Python commands
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# .\.venv\Scripts\activate.bat  # Windows CMD
# source .venv/bin/activate     # Linux/macOS

# Verify activation (should show .venv path)
which python  # Linux/macOS
where python  # Windows

# Install dependencies in isolated environment
pip install -r requirements.txt
```

**Why Virtual Environment Discipline Matters:**
- 🔒 **Isolation**: Prevents package conflicts between projects
- 🎯 **Consistency**: Ensures same versions across development/CI
- 🛡️ **Protection**: Avoids polluting system Python installation
- 🔄 **Reproducibility**: Enables reliable environment recreation

## 🐛 Troubleshooting

### Common Issues

1. **Flask server not starting:**
   ```bash
   # Check if virtual environment is activated (should show (.venv))
   pip install -r requirements.txt
   ```

2. **Test separation issues:**
   ```bash
   # Run main tests and BDD tests separately
   pytest -v                                    # Main tests only
   pytest tests/acceptance/bdd_playwright/ -v   # BDD tests only
   ```

3. **Virtual environment issues:**
   ```bash
   # Recreate virtual environment
   python -m venv .venv
   # Activate and reinstall dependencies
   ```

4. **Database issues:**
   ```bash
   # Remove database file to reset
   rm tasks.db        # Linux/macOS
   del tasks.db       # Windows
   ```

### Environment Verification

```bash
# Check Flask application health
curl http://localhost:5000/api/health
```

## 📚 Documentation

### Lab Instructions
- **Step-by-Step Guides** - `labs/` directory contains comprehensive lab instructions

### Sprint Documentation
Each sprint includes comprehensive documentation:
- **Sprint Plans** - Sprint objectives and deliverables
- **API References** - Current API endpoint documentation  
- **Architecture Documentation** - System design and patterns
- **Class Diagrams** - UML class relationships (Mermaid)
- **ERD Diagrams** - Entity relationship diagrams (Mermaid)
- **Test Cases** - Detailed test case specifications
- **Test Plans** - Testing strategy and execution plans
- **User Journey Documentation** - User flow and experience mapping

### Technical Guides
- **BDD Testing Guide** - `tests/acceptance/bdd_playwright/README.md`


## 📝 License

This is an educational project for learning software engineering practices.

## 🙋‍♂️ Support

For issues or questions:
1. Check the **sprint documentation** in `docs/sprint#/` directories
2. Review **lab instructions** in `labs/` directory  
3. Check **test plans and cases** for testing guidance
4. Review test output and error messages
5. Verify virtual environment is activated
6. Ensure Flask server is running for integration tests
7. See **BDD documentation** for acceptance testing issues

---

