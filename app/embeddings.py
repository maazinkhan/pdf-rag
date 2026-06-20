# Should convert the text to vectors
#Accepts list of text and returns list of vectors

#embed_texts(chunks) --> chunks from chunker.py

from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def embed_texts(texts: list[str]) -> list[list[float]]:
    client = genai.Client()

    embedding_responses = []

    # Generate one embedding per text chunk.
    # Passing a list to embed_content() did not return one embedding per input text.
    for t in texts:
        result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=t,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
        )

        embedding_responses.append(result.embeddings[0].values)


    if len(texts) != len(embedding_responses):
        raise ValueError("Embedding count mismatch")

    return embedding_responses

