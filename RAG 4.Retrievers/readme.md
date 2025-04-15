## What are Retrievers
A retriever is a component in LangChain that fetches relevant documents from a data source in response to a user's query.  
There are multiple types of retrievers
All retrievers in LangChain are runnables

Broadly there are two ways on which retrivers can be classified:
1. On the basis of which data source it is working with
like wikipedia, arxiv etc.
2. on the basis of which strategy it is using for searching
eg. MMR, contextual Compression etc.

## On the basis of data source
### 1. Wikipedia Retriever
A Wikipedia Retriever is a retriever that queries the Wikipedia API to fetch relevant content for a given query.
How It Works
1. You give it a query (eg.. "Albert Einstein")
2. It sends the query to Wikipedia's API
3. It retrieves the most relevant articles
4. It returns them as LangChain Document objects

How is it different from document loader?  
Document loader will directly fetch a page from wikipedia but it will search for relevant page of wikipedia and then loads it.

### 2. Vector Store Retriever
A Vector Store Retriever in LangChain is the most common type of retriever that lets you search and fetch documents from a vector store based on semantic similarity using vector embeddings.
How It Works
1. You store your documents in a vector store (like FAISS, Chroma, Weaviate)
2. Each document is converted into a dense vector using an embedding model
3. When the user enters a query:
It's also turned into a vector
The retriever compares the query vector with the stored vectors
It retrieves the top-k most similar ones

why can't we directly use `vectorstore.similarity_search` instead of `as_retriever`?
Because we can specify a search strategy with retriever. 

## on the basis of search strategy
### 1. MMR
Maximal Marginal Retriever gives diverse results(normal search could give similar kind of results, like repeat the same fact again and again)
> "How can we pick results that are not only relevant to the query but also different from each other?"   

MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.  
**Why MMR Retriever?**  
In regular similarity search, you may get documents that are:
* All very similar to each other
* Repeating the same info
* Lacking diverse perspectives  

**MMR Retriever avoids that by:**
* Picking the most relevant document first
* Then picking the next most relevant and least similar to already selected docs
And so on...

### 2. Multi-Query Retriever 

### 3. contextual Compression 