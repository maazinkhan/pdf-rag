from loader import load_pdf
from chunker import chunk_text
from embeddings import embed_texts
from storage import save_records

#1 - extract text from pdf, returns string
full_data = load_pdf("attention_is_all_you_need.pdf")

#2 - break that into chunks, returns list of chunks
chunks = chunk_text(full_data)

#3 - convert theses chunks to embeddings, returns list[list[float]]
embedded_vectors = embed_texts(chunks)

#4 - here create a list of dicts to send to save_records()
records = [
    {
        "chunk_id": i,
        "text": chunk,
        "embedding" : embedding
    }
    for i, (chunk,embedding) in enumerate(zip(chunks,embedded_vectors))
]

# for chunk_id, (chunk,embedding) in enumerate(zip(chunks,embedded_vectors)):
#     records.append({
#         "chunk_id": chunk_id,
#         "text": chunk,
#         "embedding": embedding
#     })

#5 - call save_records() to save the embeddings in a json file

save_records(records)

print(f"Indexed {len(records)} chunks")