#!/usr/bin/env bash
#
# Setup script for the 63-63 party website.
# Installs the git pre-commit hook and checks dependencies.
#
# Usage: bash scripts/setup.sh
#

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK_PATH="$PROJECT_ROOT/.git/hooks/pre-commit"

echo "63-63 Website Setup"
echo "==================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 is required but not installed."
    exit 1
fi
echo "Python3: $(python3 --version)"

# Check markdown library
if ! python3 -c "import markdown" 2>/dev/null; then
    echo "Installing Python 'markdown' library..."
    pip install markdown
fi
echo "Python markdown library: OK"

# Install pre-commit hook
cat > "$HOOK_PATH" << 'HOOK'
#!/usr/bin/env bash
#
# Pre-commit hook for 63-63 website.
# 1. Runs the build script to regenerate index.html
# 2. Stages the generated index.html
# 3. Runs tests to validate the site
#

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel)"

echo "[pre-commit] Building website..."
python3 "$PROJECT_ROOT/scripts/build.py"

echo "[pre-commit] Staging generated index.html..."
git add "$PROJECT_ROOT/index.html"

echo "[pre-commit] Running tests..."
python3 "$PROJECT_ROOT/scripts/test.py"

echo "[pre-commit] All checks passed."
HOOK

chmod +x "$HOOK_PATH"
echo ""
echo "Pre-commit hook installed at: $HOOK_PATH"

# Run initial build
echo ""
echo "Running initial build..."
python3 "$PROJECT_ROOT/scripts/build.py"

echo ""
echo "Running tests..."
python3 "$PROJECT_ROOT/scripts/test.py"

echo ""
echo "Setup complete! You can now edit content in the content/ folder."
echo "See COME-MODIFICARE-IL-SITO.md for instructions."
