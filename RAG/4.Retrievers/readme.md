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
> Sometimes a single query might not capture all the ways information is phrased in your documents.  

For example Query:  
> "How can I stay healthy?"   

Could mean:  
- What should I eat?  
- How often should I exercise?  
- How can I manage stress?  

A simple similarity search might miss documents that talk about those things but don't use the word "healthy".

1. Takes your original query
2. Uses an LLM (e.g., GPT-3.5) to generate multiple semantically different versions of that query
3. Performs retrieval for each sub-query
4. Combines and deduplicates the results

### 3. contextual Compression 
The Contextual Compression Retriever in LangChain is an advanced retriever that improves retrieval quality by compressing documents after retrieval keeping only the relevant content based on the user's query.  
**Query:**
> "What is photosynthesis?"

Retrieved Document (by a *traditional retriever*):
> "The Grand Canyon is a famous natural site.
Photosynthesis is how plants convert light into energy.
Many tourists visit every year."

**Problem:**  
- The retriever returns the entire paragraph
- Only one sentence is actually relevant to the query
- The rest is irrelevant noise that wastes context window and may confuse the LLM

What *Contextual Compression Retriever* does:  
Returns only the relevant part, e.g.  
> "Photosynthesis is how plants convert light into energy."

**How It Works**
1. Base Retriever (e.g., FAISS, Chroma) retrieves N documents.
2. A compressor (usually an LLM) is applied to each document.
3. The compressor keeps only the parts relevant to the query.
4. Irrelevant content is discarded.

**When to Use**
- Your documents are long and contain mixed information
- You want to reduce context length for LLMs
- You need to improve answer accuracy in RAG pipelines