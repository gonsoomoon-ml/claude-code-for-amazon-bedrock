# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Stock information AI Agent using Strands Agents SDK and Amazon Bedrock Claude.

## Tech Stack

- **Agent Framework**: Strands Agents SDK
- **LLM**: Amazon Bedrock Claude Sonnet
- **Stock Data**: yfinance

## Commands

```bash
# Setup environment
cd setup && bash create_env.sh

# Run agent
uv run --project setup python agent.py

# Test stock tool
uv run --project setup python test_stock_tool.py
```

## Project Structure

```
├── setup/
│   ├── create_env.sh      # Environment setup script
│   └── pyproject.toml     # Dependencies
├── tools/
│   └── stock_tool.py      # Stock price lookup tool (@tool decorator)
├── agent.py               # Main agent with BedrockModel
└── test_stock_tool.py     # Tool test script
```

## Architecture

1. User query → Agent
2. Agent → Claude (Bedrock) analyzes and decides to call tool
3. `get_stock_price()` → yfinance API
4. Result → Claude generates natural language response

## License

MIT License
