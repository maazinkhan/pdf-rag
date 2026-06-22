from retrieval import retrieve
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def build_prompt(question, context_chunks):
    """Assemble a RAG prompt from the question and retrieved chunks."""
    context = "\n\n".join(context_chunks)
    prompt = (
        "You are a helpful assistant. Answer the question using only the "
        "context below.\n"
        # 'If the answer is not in the context, say "I don\'t know."\n\n'
        f"Context:\n{context}\n\n"
        f"Question:\n{question}"
    )
    return prompt



def generate_answer(prompt: str) -> str:
    client = genai.Client(api_key=GOOGLE_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text



def answer_question(question: str) -> str:
    results = retrieve(question)

    context_chunks = [
        r["record"]["text"]
        for r in results
    ]

    prompt = build_prompt(question, context_chunks)

    return generate_answer(prompt)