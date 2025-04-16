# Langchain Learning Repository

This repository contains my learning journey and experiments with LangChain - a framework for developing applications powered by language models.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Anthropic API key (for Claude models)
- Google API key
- HuggingFace API token

### Setup

1. Clone the repository
```bash
git clone https://github.com/Upeshjeengar/Langchain.git
cd Langchain
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install langchain openai anthropic google-api-python-client transformers
```

4. Set up environment variables
   - Create a `.env` file in each project directory
   - Add your API keys (see `.env.example` for format)

## 🔑 Environment Variables

Create a `.env` file with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

⚠️ **Important**: Never commit your actual API keys to version control. The `.env` files are included in `.gitignore`.

## 📚 Learning Resources

- [LangChain Documentation](https://python.langchain.com/docs/tutorials/)
- [Campusx Yotube Videos](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)
- [OpenAI Documentation](https://platform.openai.com/docs/introduction)
- [Anthropic Claude Documentation](https://docs.anthropic.com/claude/docs)
- [HuggingFace Documentation](https://huggingface.co/docs)
## 🛠️ Projects

Each directory contains different aspects of LangChain:

1. **Langchain Models**: Experiments with various LLM integrations
2. **Langchain Prompts**: Learning prompt engineering techniques
3. **Structured Output**: Working with structured data outputs
4. **Output Parsers**: Converting LLM responses into structured formats
5. **Chains**: Combining multiple components into sequential workflows
6. **Runnables**: Building modular and reusable LangChain components

### **RAG**
RAG has four main components:
1. **Document Loaders**: used to load data from various sources into a standardized format.
2. **Text splitter**:process of breaking large chunks of text small chunks that an LLM can handle effectively.
3. **Vector databases**: a type of database designed to store, manage, and search high-dimensional vector data.
4. **Retrievers**:component in LangChain that fetches relevant documents from a data source in response to a user's query


## 📝 License

This project is for learning purposes. Feel free to use the code as reference for your own learning journey.

## ⚠️ Security Note

Make sure to:
- Keep your API keys secure
- Never commit `.env` files
- Use environment variables for sensitive information
- Review code before running it

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome through issues or pull requests. 