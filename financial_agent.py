from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 


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

## Multi AI Agent
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Search the web for relevant information.","Use tables to display thr data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize the analyst reccomendation and share the late news for NVDA", stream=True)