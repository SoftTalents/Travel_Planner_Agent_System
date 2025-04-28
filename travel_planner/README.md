# Travel Planner Agent

This project implements a travel planning agent using the Google ADK (Agent Development Kit). The agent coordinates with sub-agents to gather travel preferences from the user and provide flight and hotel suggestions, along with a day plan.

## Dependencies

*   google-adk
*   pydantic
*   datetime

You can install the dependencies using pip:

```bash
pip install google-adk pydantic python-dateutil
```

## Project Structure

*   `agent.py`: Main coordinator agent that gathers travel preferences and queries sub-agents.
*   `subagents/`: Contains sub-agents for specific tasks.
    *   `flight_agent.py`: Agent for finding flight suggestions.
    *   `hotel_agent.py`: Agent for finding hotel suggestions.
*   `tools/`: Contains utility modules.
    *   `schemas.py`: Defines the `TravelInfo` data model using Pydantic.

## Usage

1.  Install the dependencies.
2.  Run the `agent.py` file.
3.  Interact with the agent to provide your travel preferences (origin, destination, start date, end date, budget).
4.  The agent will coordinate with the sub-agents to provide flight and hotel suggestions.
5.  The agent will present a final result combining the results from both agents and a day plan.

## Example

User input:

```
I want to travel from New York to Los Angeles from 2025-05-01 to 2025-05-05 with a budget of $1000.
```

The agent will extract the travel details and provide flight and hotel suggestions within the specified budget.

## License

[Specify the license here, e.g., MIT License]