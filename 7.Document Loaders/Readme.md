# Building RAG Based applications
RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.
Benefits of using RAG
1. Use of up-to-date information
2. Better privacy
3. No limit of document size

## RAG has four main components:
1. Document Loader
2. Text splitter
3. Vector databases
4. Retrievers

## Document Loaders
Some common type of document loaders are TextLoader, PyPDFLoader, WebBaseLoader, CSVLoader

Document loaders are components in LangChain used to load data from various sources into a standardized format (usually as Document objects), which can then be used for chunking, embedding, retrieval, and generation.  
example Document object:
```
Document(
    page_content="The actual text content",
    metadata={"source": "filename.pdf", ...} 
)
```
### **TextLoader** 
It is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects.  
**Use Case** : Ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.  
**Limitation** : Works only with `.txt` files
(see `text_loader.py` for code implementation)