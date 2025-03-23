Runnables help in combining various components of lanchain like LLMs, output parsers, or retrievers etc.
> Used to connect various components sequentially to make complex workflows

# Types of ruunables
## 1. Task specific
**Definition**: These are core LangChain components that have been converted into Runnables so they can be used in pipelines.  
**Purpose**: Perform task-specific operations like LLM calls, prompting, retrieval, etc.  
**Examples**:
* `ChatOpenAI` : Runs an LLM model.  
* `PromptTemplate` : Formats prompts dynamically.  
* `Retriever` : Retrieves relevant documents.  

## 2. Runnable primitives
**Definition**: These are fundamental building blocks for structuring execution logic in Al workflows(Basically helps in connecting various task specific runnables).  
**Purpose**: They help orchestrate execution by defining how different Runnables interact (sequentially, in parallel, conditionally, etc.).
**Examples**:
* `RunnableSequence` Runs steps in order ( operator).  
* `RunnableParallel` Runs multiple steps simultaneously.  
* `RunnableMap` Maps the same input across multiple functions.  
* `RunnableBranch` Implements conditional execution (if-else logic).  
* `RunnableLambda` Wraps custom Python functions into Runnables.  
* `RunnablePassthrough` Just forwards input as output (acts as a placeholder).  

# LangChain Runnables

Runnables are the fundamental building blocks in LangChain that enable you to create complex workflows by combining various components like LLMs, output parsers, retrievers, and more.

## What are Runnables?

Runnables are objects that can be:
- Invoked with inputs
- Combined with other runnables
- Used to create complex chains of operations
- Integrated with different components of LangChain

## Key Features

1. **Composability**
   - Combine multiple components
   - Create sequential workflows
   - Build complex processing pipelines

2. **Flexibility**
   - Work with different types of inputs/outputs
   - Support async operations
   - Handle streaming responses

3. **Integration**
   - Connect with LLMs
   - Interface with output parsers
   - Work with retrievers and memory

## Basic Examples

### Simple Runnable Chain
```python
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Create components
prompt = PromptTemplate.from_template("Tell me about {topic}")
model = ChatOpenAI()

# Create chain
chain = {"topic": RunnablePassthrough()} | prompt | model

# Use chain
result = chain.invoke("quantum computing")
```

### Runnable with Multiple Steps
```python
from langchain_core.output_parsers import StrOutputParser

# Create chain with multiple steps
chain = (
    {"topic": RunnablePassthrough()} 
    | prompt 
    | model 
    | StrOutputParser()
)
```

## Advanced Usage

### 1. Parallel Processing
```python
from langchain_core.runnables import RunnableParallel

# Create parallel chain
chain = RunnableParallel({
    "facts": prompt | model,
    "summary": summary_prompt | model
})
```

### 2. Conditional Routing
```python
from langchain_core.runnables import RunnableBranch

# Create conditional chain
chain = RunnableBranch(
    (lambda x: x["type"] == "math", math_chain),
    (lambda x: x["type"] == "history", history_chain),
    default_chain=general_chain
)
```

### 3. State Management
```python
from langchain_core.runnables import RunnableWithMessageHistory

# Create chain with message history
chain = RunnableWithMessageHistory(
    prompt | model,
    lambda session_id: memory
)
```

## Common Use Cases

1. **Document Processing**
   - Extract information
   - Generate summaries
   - Answer questions

2. **Conversation Systems**
   - Maintain context
   - Handle multi-turn dialogues
   - Manage memory

3. **Data Transformation**
   - Format conversion
   - Content filtering
   - Output structuring

## Best Practices

1. **Design**
   - Keep runnables focused and modular
   - Use appropriate components for each task
   - Plan error handling

2. **Implementation**
   - Start with simple chains
   - Test with various inputs
   - Monitor performance

3. **Maintenance**
   - Document component interactions
   - Version control your runnables
   - Regular testing

## Advantages

1. **Modularity**
   - Easy to modify individual components
   - Reusable across applications
   - Clear separation of concerns

2. **Scalability**
   - Handle complex workflows
   - Support async operations
   - Manage large datasets

3. **Flexibility**
   - Work with different models
   - Support various input/output types
   - Easy to extend

## Resources

- [LangChain Documentation](https://python.langchain.com/docs/modules/runnables/)
- [Runnable Examples](https://python.langchain.com/docs/modules/runnables/examples/)
- [Advanced Runnable Patterns](https://python.langchain.com/docs/modules/runnables/advanced/)
