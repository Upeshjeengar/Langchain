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

### PyPDF
PyPDFLoader is a document loader in LangChain used to load content from PDF files and convert each page into a Document object. 
```
[
    Document(page_content="Text from page 1", metadata={"page": 0, "source": "file.pdf"}),
    Document(page_content="Text from page 2", metadata={"page": 1, "source": "file.pdf"}),
    ....
]
```
**Limitations**: It uses the PyPDF library under the hood not great with scanned PDFs or complex layouts.
(see `pdf_loader.py` for code implementation)

### PDF Loaders Guide

This table provides guidance on selecting the best PDF loader based on different use cases.

| Use Case                        | Recommended Loader                           |
|---------------------------------|---------------------------------------------|
| Simple, clean PDFs              | `PyPDFLoader`                               |
| PDFs with tables/columns        | `PDFPlumberLoader`                          |
| Scanned/image PDFs              | `UnstructuredPDFLoader` or `AmazonTextractPDFLoader` |
| Need layout and image data      | `PyMuPDFLoader`                             |
| Want best structure extraction  | `UnstructuredPDFLoader`                     |
---------------------------------------------------------------------------------

### Directory Loader  
DirectoryLoader is a document loader that lets you load multiple documents from a directory (folder) of files.  

|Glob Pattern  | What It Loads|
|---------------|------------|
|"`**/*.txt`"| All `.txt` files in all subfolders|
|"`*.pdf`"   | All `.pdf` files in the root directory|
|"`data/*.csv`"|All `.csv` files in the data/folder|
|`**/*`|All files(any type, all folders)|
where *= recursive search through subfolders and `glob` is a pattern specifying parameter(to be passed in `DirectoryLoader` class)

(see `directory_loader.py` for code implementation)

### Load vs Lazy Load
|load()|  lazy_load()|
|--------|-------------|
|Eager Loading (loads everything at once).|Lazy Loading (loads on demand).|
Returns: A list of Document objects.|Returns: A generator of Document objects.
Loads all documents immediately into memory.|Documents are not all loaded at once, they're fetched one at a time as needed.
**Best when**: The number of documents is small.You want everything loaded upfront. |**Best when**: You're dealing with large documents or lots of files.You want to stream processing (e.g. chunking, embedding) without using lots of memory.

