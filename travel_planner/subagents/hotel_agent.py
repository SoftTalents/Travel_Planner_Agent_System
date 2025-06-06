from google.adk import Agent

hotel_agent = Agent(
    name="hotel_agent",
    model="gemini-2.0-flash-exp",
    description="An agent that can help you find hotels and accommodation information.",
    instruction= """
                  You are a hotel booking agent. The coordinator will give you:
                  - destination
                  - start_date
                  - end_date
                  - budget_amount
                  - budget_currency
                  
                  Return 1-2 mock hotel suggestions including:
                  - Hotel name
                  - Nightly rate and total cost in the given currency
                  - Main features
                  
                  Ensure the total price fits the budget.
                 """
)