


def chunk_text(text:str, chunk_size=1000, overlap=200) -> list[str]:
    start = 0
    chunks=[]

    step = max(1, chunk_size - overlap)

    while start < len(text):
        chunks.append(text[start:start+chunk_size])
        start += step
    return chunks

