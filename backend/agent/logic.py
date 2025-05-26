from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from .tools import get_tools

def run_agent(query):
    llm = ChatOpenAI(model="gpt-4")
    tools = get_tools()
    agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description")
    return agent.run(query)
