from langchain.tools import DuckDuckGoSearchRun

def get_tools():
    search = DuckDuckGoSearchRun()
    return [search]
