# Text Splitters
Text Splitting is the process of breaking large chunks of text (like articles, PDFs, HTML pages, or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively.

* **Overcoming model limitations**: Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.
* **Downstream tasks** - Text Splitting improves nearly every LLM powered task.  
Embedding : Short chunks yield more accurate vectors   
Semantic Search: Search results point to focused info, not noise   
Summarization: Prevents hallucination and topic drift  
* **Optimizing computational resources**: Working with smaller chunks of text can be
more memory-efficient and allow for better parallelization of processing tasks.

https://chunkviz.up.railway.app/   
4 techniques to split text:  
1.  **Length Based Splitting:** Dividing into uniform size chunks,Deciding chunk size-on the basis of characters or tokens.
**Advantage:** Simple and fast  
**Disadvantage:** Grammatical mistakes   
see `length_based.py` for code 
2. **Text structure based:**: Separting on the basis of end of para or line or word or character, it recursively splits to maintain the prespecified chunk size, first it splits on basis of para, if chunk size is bigger then it splits on basis of line, then word and then character basis.  
It is most commonly used technique.   
see `text_structure_based.py` for code
3. **Document structured basis**: Used for special kinds of texts like codes, markdown files etc.  
see `python_code_splitting.py`, `markdown_splitting.py` for codes.
4. **Sematic meaning based**: Maitains context between chunks

for eg. in below text
```
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.
Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety
```
first or second method will divide into 2 chunks on basis of size but ideally there should be 3 chunks(farmer, IPL, terrorism)

How to do this?
compare sentence wise embedding vector comparison.
see `semantic_meaning_based.py` for code