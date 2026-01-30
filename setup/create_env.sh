#!/bin/bash
set -e

echo "=============================================="
echo "Stock Agent - Environment Setup"
echo "=============================================="

# Navigate to setup directory
cd "$(dirname "$0")"

# Install dependencies using uv
echo ""
echo "Installing dependencies..."
uv sync --quiet

# Verify installation
echo ""
echo "Verifying installation..."
uv run python -c "import strands; print('  ✓ strands-agents installed')"
uv run python -c "import yfinance; print('  ✓ yfinance installed')"
uv run python -c "import boto3; print('  ✓ boto3 installed')"

echo ""
echo "=============================================="
echo "Setup Complete!"
echo "=============================================="
echo ""
echo "Next steps:"
echo "  1. Configure AWS credentials: aws configure"
echo "  2. Run the agent: uv run python agent.py"
echo ""
