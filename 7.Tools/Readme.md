# Tools
A tool is just a Python function (or API) that is packaged in a way the LLM can understand and call when needed.

Official Documentation : https://python.langchain.com/docs/integrations/tools/ 
- LLMs (like GPT) are great at: Reasoning, Language generation   

But they can't do things like:  
- Access live data (weather, news)
- Do reliable math
- Call APIs
- Run code
- Interact with a database

Types of tools:
- Build-in tools
- custom tools  

How Tools fits into the `Agent ecosystem`?  
An Al agent is an LLM-powered system that can autonomously think, decide, and take actions using external tools or APIs to achieve a goal.
Simply saying Agent = LLMs(for reasoning and decision making) with access to tools(for performing action)

## 1. Built-in Tools
A built-in tool is a tool that LangChain already provides for you it's pre-built, production-ready, and requires minimal or no setup.  
You don't have to write the function logic yourself you just import and use it.  

| Tool Name             | Description                |
| --------------------- | -------------------------- |
| `DuckDuckGoSearchRun`   | Web search via DuckDuckGo  |
| `WikipediaQueryRun`     | Wikipedia summary          |
| `PythonREPLTool`        | Run raw Python code        |
| `ShellTool`             | Run shell commands         |
| `RequestsGetTool`       | Make HTTP GET requests     |
| `GmailSendMessageTool`  | Send emails via Gmail      |
| `SlackSendMessageTool`  | Post message to Slack      |
| `SQLDatabaseQueryTool`  | Run SQL queries            |

## 2. Custom Tools
A custom tool is a tool that you define yourself.  
Use them when:
- You want to call your own APIs
- You want to encapsulate business logic
- You want the LLM to interact with your database, product, or app

Ways to create custom Tools: 
- using `@tool` decorator
- using `StructuredTool` & `Pydantic`:
A Structured Tool in LangChain is a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model.
- Using `BaseTool` class: BaseTool is the abstract base class for all tools in LangChain. It defines the core structure and interface that any tool must follow, whether it's a simple one-liner or a fully customized function.
All other tool types like @tool, Structured Tool are built on top of BaseTool

# Tool calling
Tool Calling is the process where the LLM (language model) decides, during a conversation or task, that it needs to use a specific tool (function) and generates a structured output with:
* the name of the tool
* the arguments to call it with  

▲The LLM does not actually run the tool - it just suggests the tool and the input arguments. The actual execution is handled by LangChain or you

# Tool Binding
Tool Binding is the step where you register tools with a Language Model (LLM) so that:
1. The LLM knows what tools are available
2. It knows what each tool does (via description)
3. It knows what input format to use (via schema)

# Tool execution
LLM will not run code by itself, it will just suggest which tools you can use.  
Tool Execution is the step where the actual Python function (tool) is run using the input arguments that the
LLM suggested during tool calling.  
In simpler words:  
The LLM says:  
`Hey, call the multiply tool with a=8 and b=7.`  
Tool Execution is when you or LangChain actually run:  
`multiply(a=8, b=7)`
and get the result: `56`