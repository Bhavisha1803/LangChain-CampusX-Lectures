from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('Most trending news in the world today')

# print(results)
# print('-----------------------------')
# print(search_tool.name)
# print(search_tool.description)
# print(search_tool.args)

from langchain_community.tools import ShellTool

shell_tool = ShellTool()

results2= shell_tool.invoke('cd .. \nls')

# print(results2)

