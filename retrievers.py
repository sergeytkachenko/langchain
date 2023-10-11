import os
import weaviate
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.retrievers import WeaviateHybridSearchRetriever
from langchain.schema import Document
from langchain.vectorstores import Weaviate


def get_weaviate_openai_retriever(index ="Academy5") -> WeaviateHybridSearchRetriever:
    WEAVIATE_URL = "http://localhost:8080"
    client = weaviate.Client(
        url=WEAVIATE_URL,
        additional_headers={
            "X-Openai-Api-Key": os.getenv("OPENAI_API_KEY"),
        },
    )
    retriever = WeaviateHybridSearchRetriever(
        client=client,
        index_name=index,
        text_key="content",
        attributes=["source"],
        create_schema_if_missing=True,
    )
    return retriever

def get_weaviate_huggingface_retriever(
        documents: list[Document],
        index ="AcademyHuggingface1"
) -> WeaviateHybridSearchRetriever:
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=os.getenv("HF_API_KEY"),
        model_name="sentence-transformers/all-MiniLM-l6-v2"
    )
    # client = weaviate.Client(
    #     url="http://localhost:8080",
    #     additional_headers={
    #         'X-HuggingFace-Api-Key': os.getenv("HF_API_KEY")
    #     },
    # )
    # retriever = WeaviateHybridSearchRetriever(
    #     client=client,
    #     embeddings=embeddings,
    #     embedding=embeddings,
    #     index_name=index,
    #     text_key="content",
    #     attributes=["source"],
    #     create_schema_if_missing=True,
    # )
    retriever = Weaviate.from_documents(
        weaviate_url="http://localhost:8080",
        additional_headers={
            'X-HuggingFace-Api-Key': os.getenv("HF_API_KEY")
        },
        documents=documents,
        embedding=embeddings,
        index_name=index,
        text_key="content",
        attributes=["source"],
        create_schema_if_missing=True,
    )
    # retriever.add_documents(documents)
    return retriever

def weaviate_search(
    retriever: WeaviateHybridSearchRetriever,
    query: str
):
    print("start weaviate hybrid search by query: ", query)
    results = retriever.get_relevant_documents(
        query,
        score=True,
    )
    print(list(map(lambda x: x.metadata["source"], results)))
    return results, retriever
