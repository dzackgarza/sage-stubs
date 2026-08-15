#!/usr/bin/env bash
# Bootstrap script: install uv and just if missing
# Run this once to set up development tools for sage-stubs
# Usage: ./bootstrap.sh

set -e

echo "=== sage-stubs bootstrap ==="

# Install uv if missing
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Source the environment if needed
    if [ -f "$HOME/.local/bin/env" ]; then
        source "$HOME/.local/bin/env"
    fi
else
    echo "✓ uv already installed"
fi

# Install just if missing
if ! command -v just &> /dev/null; then
    echo "Installing just..."
    # Create ~/bin if it doesn't exist
    mkdir -p ~/bin
    curl -LSsf https://just.systems/install.sh | bash -s '--' --to ~/bin
    
    # Check if ~/bin is in PATH
    if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
        echo ""
        echo "⚠️  WARNING: ~/bin is not in your PATH"
        echo "   Add it to your shell config (e.g., ~/.bashrc or ~/.zshrc):"
        echo "   export PATH=\"\$HOME/bin:\$PATH\""
        echo ""
        echo "Then run: source ~/.bashrc  (or restart your terminal)"
        echo ""
        exit 1
    fi
else
    echo "✓ just already installed"
fi

echo ""
echo "=== Bootstrap complete ==="
echo "Next steps:"
echo "  just setup    # Configure git hooks and initialize submodules"
echo "  just check    # Run full quality pipeline"
