Formal defintion: Output Parsers in LangChain help convert raw LLM responses into structured formats like JSON, CSV, Pydantic models, and more. They ensure consistency, validation, and ease of use in applications.

**Output parsers** for the LLM which can not give structured output(like in the last part we had seen `model.with_structured_output` can be used to get structured output of LLM but it does not work with all models)

**Four types of output parser:**
## 1. StrOutputParser
The StrOutputParser is the simplest output parser in LangChain. It is used to parse the output of a Language Model (LLM) and return it as a plain string.
It returns output in form of dictionary type(exactly similar to calling `result.content` from `model.invoke`)  
**Then** what's the **difference**?
See the difference by example: Prompt -> Detailed output using LLM -> summarize it
Outputparsers make this pipeline easier


## 2. JSONOutputParser
The JSON Output Parser in LangChain is a utility that helps structure LLM outputs into JSON format.  
But Even with defined schemas, LLMs might generate non-compliant data
## 3. StructuredOutputParser
StructuredOutputParser is an output parser in LangChain that helps extract structured JSON data from LLM responses based on predefined field schemas.  
It works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows a structured format.
Shortcoming: Can not do data validation.

## 4. PydanticOutputParser
• What is PydanticOutputParser in LangChain?
PydanticOutputParser is a structured output parser in LangChain that uses Pydantic models to enforce schema validation when processing LLM responses.
Why Use PydanticOutputParser?  
Strict Schema Enforcement Ensures that LLM responses follow a well-defined structure.    
Type Safety Automatically converts LLM outputs into Python objects.  
Easy Validation - Uses Pydantic's built-in validation to catch incorrect or missing data.  
Seamless Integration - Works well with other LangChain components.