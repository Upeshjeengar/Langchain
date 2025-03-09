# Langchain Models

This directory contains implementations and examples of different types of language models using LangChain. It demonstrates how to work with various model types and providers through a unified interface.

## 📂 Directory Structure

### 1. LLMs
Basic Language Model implementations focusing on:
- Text completion
- Direct model interactions
- Single-turn responses
- Model parameter configurations

### 2. ChatModels
Chat-specific model implementations featuring:
- Multi-turn conversations
- Chat history management
- Message role handling (system, user, assistant)
- Conversational memory implementations

### 3. EmbeddedModels
Text embedding and vector operations including:
- Text embeddings generation
- Semantic search
- Document similarity
- Vector store integrations

## 🔧 Setup

1. Ensure you have the required dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

## 📚 Key Features

- Multiple model provider integrations (OpenAI, Anthropic, HuggingFace)
- Different model types and use cases
- Example implementations for each model type
- Best practices for model interaction
- Parameter tuning examples

## 🛠️ Usage

Each subdirectory contains specific examples and implementations:

- `1.LLMs/`: Basic text generation and completion tasks
- `2.ChatModels/`: Interactive chat applications and conversational agents
- `3.EmbeddedModels/`: Text embedding and semantic search applications

## 📋 Dependencies

Key dependencies include:
```
langchain
openai
anthropic
google-api-python-client
transformers
python-dotenv
```

Full dependencies are listed in `requirements.txt`

## ⚠️ Important Notes

- Keep API keys secure and never commit them to version control
- Monitor API usage to manage costs
- Different models may have different rate limits and pricing
- Consider model performance vs cost tradeoffs

## 🔍 Examples

Each model type directory contains example scripts demonstrating:
- Basic usage
- Advanced configurations
- Error handling
- Best practices
- Performance optimization

## 📖 Learning Resources

- [LangChain Model Reference](https://python.langchain.com/docs/modules/model_io/models/)
- [OpenAI Model Documentation](https://platform.openai.com/docs/models)
- [Claude Model Documentation](https://docs.anthropic.com/claude/docs/models-overview)
- [HuggingFace Models](https://huggingface.co/models)