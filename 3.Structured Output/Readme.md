## Structured Output

In LangChain, structured output refers to the practice of having language models return responses in a well-defined data format (for example, JSON), rather than free-form text. This makes the model output easier to parse and work with programmatically.

**[Prompt]** Can you create a one-day travel itinerary for Paris?  
[LLM's Unstructured Response]
Here's a suggested itinerary:   
Morning: Visit the Eiffel Tower.  
Afternoon: Walk through the Louvre Museum.  
Evening: Enjoy dinner at a Seine riverside café.
[JSON enforced output]  
[  
{"time": "Morning", "activity": "Visit the Eiffel Tower"},  
{"time": "Afternoon", "activity": "Walk through the Louvre Museum"},  
{"time": "Evening", "activity": "Enjoy dinner at a Seine riverside café"}  
]


## Why we need structured output?
- Data Extraction
- API Building
- Agents

## TypedDict
It is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.  
Why use TypedDict?    
* It tells Python what keys are required and what types of values they should have.  
* It does not validate data at runtime (it just helps with type hints for better coding).
TypedDict   
> * simple Typed Dict  
> * Annotated Typed Dict  
> * Literal  
> * More complex with pros and cons  

## Pydantic
Pydantic is a data validation and data parsing library for Python. It ensures that the data you work with is correct, structured, and type-safe

## JSON 
JSON format works with all languages

## When to use what
### Use TypedDict if:
* You only need type hints (basic structure enforcement).
* You don't need validation (e.g., checking numbers are positive).
* You trust the LLM to return correct data.
### Use Pydantic if:
* You need data validation (e.g., sentiment must be "positive", "neutral", or "negative").
* You need default values if the LLM misses fields.
* You want automatic type conversion (e.g., "100" 100).
### Use JSON Schema if:
* You don't want to import extra Python libraries (Pydantic).
* You need validation but don't need Python objects.
* You want to define structure in a standard JSON format

## Feature Comparison: TypedDict vs. Pydantic vs. JSON Schema

| Feature                  | TypedDict ✅ | Pydantic 🚀 | JSON Schema 🌍 |
|--------------------------|------------|------------|---------------|
| Basic structure         | ✅          | ✅          | ✅             |
| Type enforcement       | ✅          | ✅          | ✅             |
| Data validation        | ❌          | ✅          | ✅             |
| Default values         | ❌          | ✅          | ❌             |
| Automatic conversion   | ❌          | ✅          | ❌             |
| Cross-language compatibility | ❌      | ❌          | ✅             |
