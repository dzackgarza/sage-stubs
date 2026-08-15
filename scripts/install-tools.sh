#!/usr/bin/env bash
set -euo pipefail

echo "Installing uv..."
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "uv already installed"
fi

echo "Installing just..."
if ! command -v just &> /dev/null; then
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v apt &> /dev/null; then
            sudo apt update && sudo apt install -y just
        elif command -v dnf &> /dev/null; then
            sudo dnf install -y just
        elif command -v pacman &> /dev/null; then
            sudo pacman -S --noconfirm just
        else
            cargo install just
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install just
    else
        cargo install just
    fi
else
    echo "just already installed"
fi

echo "Verifying installations..."
uv --version
just --version

echo "Setup complete!"
