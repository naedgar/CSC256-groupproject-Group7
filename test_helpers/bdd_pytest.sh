# scripts/bdd_pytest.sh

# BDD pytest wrapper script for Linux/macOS (equivalent to bdd_pytest.ps1)
#
# Examples:
#   ./scripts/bdd_pytest.sh --headed --junit --html
#   ./scripts/bdd_pytest.sh --junit --html  # headless mode
#   ./scripts/bdd_pytest.sh --dry-run --headed --junit --html
#

# Default values
HEADED=false
JUNIT=false
HTML=false
DRY_RUN=false
FEATURE="tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --headed)
            HEADED=true
            shift
            ;;
        --junit)
            JUNIT=true
            shift
            ;;
        --html)
            HTML=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --feature)
            FEATURE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--headed] [--junit] [--html] [--dry-run] [--feature <path>]"
            exit 1
            ;;
    esac
done

# Try to activate virtual environment if present
if [ -f ".venv/bin/activate" ]; then
    echo "Activating venv: .venv/bin/activate"
    source .venv/bin/activate
elif [ -f "venv/bin/activate" ]; then
    echo "Activating venv: venv/bin/activate"
    source venv/bin/activate
else
    echo "No virtual environment found - ensure your virtualenv is active"
fi

# HEADLESS control
if [ "$HEADED" = true ]; then
    echo "Running in HEADED mode (HEADLESS=false)"
    export HEADLESS=false
else
    echo "Running in HEADLESS mode (HEADLESS=true)"
    export HEADLESS=true
fi

# Build pytest command arguments
PYTEST_ARGS=("--capture=no" "-q" "-x" "--maxfail=1" "$FEATURE")

# Ensure results directory exists if we need it
if [ "$JUNIT" = true ] || [ "$HTML" = true ]; then
    mkdir -p results
fi

if [ "$JUNIT" = true ]; then
    JUNIT_PATH="results/junit.xml"
    PYTEST_ARGS+=("--junitxml=$JUNIT_PATH")
    echo "JUnit output: $JUNIT_PATH"
fi

if [ "$HTML" = true ]; then
    HTML_PATH="results/report.html"
    PYTEST_ARGS+=("--html=$HTML_PATH" "--self-contained-html")
    echo "HTML report: $HTML_PATH"
fi

# Build the complete command
CMD="pytest ${PYTEST_ARGS[*]}"

if [ "$DRY_RUN" = true ]; then
    echo "DRY RUN: $CMD"
    exit 0
fi

echo "Running: $CMD"
eval "$CMD"

# Propagate exit code
exit $?