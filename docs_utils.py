from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.schema import Document
from langchain.text_splitter import LatexTextSplitter

def get_academy_docs() -> list[Document]:
    loader = DirectoryLoader(
        './docs',  # docs-small
        use_multithreading=True,
        show_progress=True,
        loader_cls=TextLoader,
    )
    docs = loader.load()
    # splitter = MarkdownTextSplitter(
    #     chunk_size=2500,
    #     chunk_overlap=200
    # )
    splitter = LatexTextSplitter(
        chunk_size=2500,
        chunk_overlap=200
    )
    splits_documents = splitter.split_documents(docs)
    print("load document chunks: ", len(docs))
    return splits_documents
