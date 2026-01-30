import sys
sys.path.insert(0, '.')

from strands import Agent
from strands.models import BedrockModel
from tools.stock_tool import get_stock_price


def main():
    # Create Bedrock model with Claude Sonnet
    model = BedrockModel(
        model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
        region_name="us-west-2",
    )

    # Create agent with stock tool
    agent = Agent(
        model=model,
        tools=[get_stock_price],
        system_prompt="You are a helpful stock information assistant. Use the get_stock_price tool to look up current stock prices when users ask about stocks.",
    )

    print("Stock Agent Ready! (type 'quit' to exit)")
    print("-" * 40)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        if not user_input:
            continue

        response = agent(user_input)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    main()
