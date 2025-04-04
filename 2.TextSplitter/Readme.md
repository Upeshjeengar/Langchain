# Text Splitters
Text Splitting is the process of breaking large chunks of text (like articles, PDFs, HTML pages, or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively.

* **Overcoming model limitations**: Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.
* **Downstream tasks** - Text Splitting improves nearly every LLM powered task.  
Embedding : Short chunks yield more accurate vectors   
Semantic Search: Search results point to focused info, not noise   
Summarization: Prevents hallucination and topic drift  
* **Optimizing computational resources**: Working with smaller chunks of text can be
more memory-efficient and allow for better parallelization of processing tasks.

4 techniques to split text:  
1.  **Length Based Splitting:** Dividing into uniform size chunks,Deciding chunk size-on the basis of characters or tokens.
https://chunkviz.up.railway.app/   
**Advantage:** Simple and fast  
**Disadvantage:** Grammatical mistakes  
2. **Text structure based:**: Separting on the basis of end of para or line or word or character, it recursively splits to maintain the prespecified chunk size, first it splits on basis of para, if chunk size is bigger then it splits on basis of line, then word and then character basis.