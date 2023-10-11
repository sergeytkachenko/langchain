from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.embeddings import Embeddings
from langchain.vectorstores import ElasticsearchStore
from prettytable import PrettyTable, ALL, FRAME

from indexing_elasticsearch import es_indexing, es_search
from questions import questions

huggingface_models = [
    {
        "name": "multilinguale5large",
        "embedding_endpoint": "https://h9em6m9mades5mmn.us-east-1.aws.endpoints.huggingface.cloud",
        "vector_index": "multilingual_e5_large".lower(),
        "embedding": None
    },
    {
        "name": "BAAIbgelargeenv15",
        "embedding_endpoint": "https://uzzsvg0w7zgyuf6d.eu-west-1.aws.endpoints.huggingface.cloud",
        "vector_index": "BAAI__bge-large-en-v1.5".lower(),
        "embedding": None
    },
    {
        "name": "openai",
        "embedding_endpoint": None,
        "embedding": OpenAIEmbeddings(),
        "vector_index": "openai"
    }
]

def similarity_search_with_score_by_model_name(model_name: str, question: str):
    target_model = None
    for model in huggingface_models:
        if model["name"] == model_name:
            target_model = model
            break
    if target_model is None:
        raise Exception("target_model not found by ", model_name)
    embedding: Embeddings = target_model["embedding"]
    embedding_endpoint = target_model["embedding_endpoint"]
    index_name = target_model["vector_index"]
    retriever = es_indexing(
        index_name=index_name,
        embedding=embedding,
        embedding_endpoint=embedding_endpoint,
        load_files=False,
        hybrid_search=True
    )
    return es_search(retriever, query=question)

def indexing_documents():
    for model in huggingface_models:
        embedding: Embeddings = model["embedding"]
        embedding_endpoint = model["embedding_endpoint"]
        index_name = model["vector_index"]
        es_indexing(
            index_name=index_name,
            embedding=embedding,
            embedding_endpoint=embedding_endpoint,
            load_files=True
        )

def questions_search():
    columns = ['']
    rows = []
    for model in huggingface_models:
        columns.append(model["name"])

    for question in questions:
        row = [question]
        for model in huggingface_models:
            response = similarity_search_with_score_by_model_name(model["name"], question)
            content = ""
            for res in response:
                [score, doc_name] = res
                doc_name = str(doc_name).replace("docs/", "")
                content += "{score} {doc_name}\n".format(score=score, doc_name=doc_name)
            row.append(content)
        rows.append(row)

    tab = PrettyTable(columns)
    tab.add_rows(rows)
    tab.hrules = ALL
    tab.vrules = ALL
    tab.int_format = '8'
    tab.padding_width = 2
    tab.junction_char = '.'
    print(tab)

def search_relevant_docs(retriever: ElasticsearchStore):
    for question in questions:
        print(question)
        es_search(retriever, query=question)
        print('---------------------------')


def openai_start(load_files=False):
    index_name = "openai".lower()
    embedding = OpenAIEmbeddings()
    retriever = es_indexing(
        index_name=index_name,
        embedding=embedding,
        load_files=load_files,
    )
    search_relevant_docs(retriever)


def bge_large_en_start(load_files=False):
    embedding_endpoint = "https://uzzsvg0w7zgyuf6d.eu-west-1.aws.endpoints.huggingface.cloud"
    index_name = "BAAI__bge-large-en-v1.5".lower()
    retriever = es_indexing(
        index_name=index_name,
        embedding_endpoint=embedding_endpoint,
        load_files=load_files,
    )
    search_relevant_docs(retriever)


def multilingual_e5_large(load_files=False):
    embedding_endpoint = "https://h9em6m9mades5mmn.us-east-1.aws.endpoints.huggingface.cloud"
    index_name = "multilingual_e5_large".lower()
    retriever = es_indexing(
        index_name=index_name,
        embedding_endpoint=embedding_endpoint,
        load_files=load_files,
    )
    search_relevant_docs(retriever)
