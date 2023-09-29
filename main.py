from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.document_loaders.sitemap import SitemapLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import AsyncHtmlLoader
from langchain.text_splitter import MarkdownTextSplitter
from langchain.text_splitter import LatexTextSplitter
from langchain.vectorstores.elasticsearch import ElasticsearchStore
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.vectorstores import Pinecone
from langchain.vectorstores.utils import DistanceStrategy
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import os
from elasticsearch import Elasticsearch
from html.parser import HTMLParser
import numpy as np
import json
from bs4 import BeautifulSoup
import re
import markdownify
import shutil
from langchain.document_transformers import Html2TextTransformer
import pinecone

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi():
    # loader = DirectoryLoader(
    #     './docs', # docs-small
    #     use_multithreading=True,
    #     show_progress=True,
    # )
    # docs = loader.load()
    # # splitter = MarkdownTextSplitter(
    # #     chunk_size=1500,
    # #     chunk_overlap=200
    # # )
    # splitter = LatexTextSplitter(
    #     chunk_size=2500,
    #     chunk_overlap=200
    # )
    # splits_documents = splitter.split_documents(docs)
    os.environ["OPENAI_API_KEY"] = "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"

    embedding = OpenAIEmbeddings()
    client = Elasticsearch(
        # hosts=["http://localhost:9200"],
        cloud_id="academy:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGRiM2MzNWE3NDJjNDRhZGE4OGY4YjYwOTUxOWM0YTg4JGFhZThmMWM1NTdhYTRmMTZhYTY5YzlkNzg2YzRmYTM4",
        request_timeout=280,
        retry_on_timeout=True,
        max_retries=2,
        basic_auth=("elastic", "bbOUCV7nDnK8r05DjtRz5zfj")
    )
    client.options(
        request_timeout=280
    ).cluster.health(
        timeout="280s",
        master_timeout="280s",
    )
    store = ElasticsearchStore(
        embedding=embedding,
        index_name="academy-from-md-latex-text",
        vector_query_field="embedding",
        strategy=ElasticsearchStore.ApproxRetrievalStrategy(
            hybrid=False,
        ),
        distance_strategy= DistanceStrategy.COSINE,
        es_connection=client
    )
    # store = ElasticsearchStore.from_documents(
    #     documents=splits_documents,
    #     embedding=embedding,
    #     index_name="academy-from-md-latex-text",
    #     vector_query_field="embedding",
    #     strategy=ElasticsearchStore.ApproxRetrievalStrategy(
    #         hybrid=True,
    #     ),
    #     distance_strategy="COSINE",
    #     es_connection=client
    # )
    # store.client.indices.refresh(index="academy-from-md-latex-text")
    query = "How install global search in creatio?"
    results = store.similarity_search(query)
    print(list(map(lambda x: x.metadata["source"], results)))

    # os.environ["PINECONE_API_KEY"] = "a6da2728-13bf-4dce-b7d7-628fe82b64dd"
    # os.environ["PINECONE_ENV"] = "gcp-starter"
    # pinecone.init(
    #     api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
    #     environment=os.getenv("PINECONE_ENV"),  # next to api key in console
    # )
    #
    # index_name = "academy"

    # First, check if our index already exists. If it doesn't, we create it
    # if index_name not in pinecone.list_indexes():
    #     # we create a new index
    #     pinecone.create_index(
    #         name=index_name,
    #         metric='cosine',
    #         dimension=1536
    #     )
    # embedding = OpenAIEmbeddings()
    #docsearch = Pinecone.from_documents(docs, embedding, index_name=index_name)

    # if you already have an index, you can load it like this
    # docsearch = Pinecone.from_existing_index(index_name, embeddings)


    # embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    # store = Chroma.from_documents(splits_documents, embedding_function)



    # html2text = Html2TextTransformer()
    # docs_transformed = html2text.transform_documents(docs)
    # print(docs_transformed)
    # markdown_text = markdownify.markdownify(docs[0].page_content)
    # print(docs)
    #
    # # loader1 = TextLoader("gs.md", encoding="utf-8")
    # # docs1 = loader1.load()
    # # print(docs1)


    # text_splitter = MarkdownTextSplitter()
    # docssplit = text_splitter.split_documents(docs1)
    # print(docssplit)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
