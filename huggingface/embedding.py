from concurrent.futures import ThreadPoolExecutor
from typing import List

from langchain.schema.embeddings import Embeddings


class HuggingfaceAwsApiEmbedding(Embeddings):
    API_URL = ""
    headers = {
        "Authorization": "Bearer RNonEILYmHzpMWugBiPaQqBMOGYpxzxEYLQLOppZLjjEmQSwTIATmxluFwmxXXkbimrgIriBxAOEmkwzAPZJQavdFdyRCpstcBHFFwUHILZGqmkVyrWVeOudebfKjEJQ",
        "Content-Type": "application/json"
    }

    def __init__(self, embedding_endpoint):
        # print("embedding endpoint:", embedding_endpoint)
        self.API_URL = embedding_endpoint

    def embed_query(self, text: str) -> List[float]:
        output = self._query({"inputs": text, })
        return output

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        print("start embed documents length::", len(texts))
        result = []
        pool = ThreadPoolExecutor(max_workers=5)
        def fetch(text):
            return self._query({"inputs": text})

        for embedding in pool.map(fetch, texts):
            result.append(embedding)

        return result

    def _query(self, payload):
        import requests
        response = requests.post(self.API_URL, headers=HuggingfaceAwsApiEmbedding.headers, json=payload)
        json = response.json()
        return json["embeddings"]