from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load() # below for loop will take time and will prinit everything once
docs = loader.lazy_load() # will load one by one and remove previous one

for document in docs:
    print(document.metadata)