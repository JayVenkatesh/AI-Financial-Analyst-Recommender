from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 
from dotenv import load_dotenv
import phi.api

import os
import phi
from phi.playground import Playground, serve_playground_app

# Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## Web Search Agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for relevant information.",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include the Sources"],
    show_tool_calls=True,
    markdown=True
)

## Financial Agent
finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True, stock_fundamentals=True),
        ],
        instructions = ["Use tables to display thr data"],
        show_tool_calls=True,
        markdown=True
)

app = Playground(agents=[web_search_agent, finance_agent]).get_app()
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)