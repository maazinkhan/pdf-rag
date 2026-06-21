from storage import load_records
from embeddings import embed_texts
import numpy as np


def cosine_similarity(a,b) -> float:
    score = np.dot(a, b) / (
            np.linalg.norm(a) * np.linalg.norm(b)
    )
    return score

def retrieve(question: str, k: int = 5):
    # create a list of dicts to append score and the record
    results = []

    # load all indexed records
    records = load_records()

    # Get embedding of the users question,passing it as a list -->embed_texts([question])
    # and since embed_texts() returns list[list[float]], for one string/element grab the 0th index and store
    question_embedding = embed_texts([question])[0]

    # get the scores
    for record in records:
        score = cosine_similarity(
            question_embedding,
            record["embedding"]
        )
        results.append({
            "score":score,
            "record": record
        })

    # sort by similarity (highest first)
    results.sort(key=lambda x: x["score"], reverse=True)

    # take top-k
    top_results = results[:k]

    return top_results
