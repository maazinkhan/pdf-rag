# pdf-rag
My first project to build a rag app without using any frameworks

## 1. Project Overview

### PDF RAG with Gemini

A simple Retrieval-Augmented Generation (RAG) application built from scratch.

Features:
- Load a PDF
- Chunk text
- Generate Gemini embeddings
- Store embeddings as JSON
- Retrieve relevant chunks using cosine similarity
- Generate answers using Gemini


## 2. Installation

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt
```

## 3. API Key Setup

```markdown
## Gemini API Key

Create a .env file:

```env
GOOGLE_API_KEY=your_api_key_here
```

## 4. Index the PDF

```markdown
## Build the Index

Place your PDF inside:

data/docs/

Run:

```bash
python3 index.py
```
This will:

1. Load the PDF
2. Create chunks
3. Generate embeddings
4. Save records to data/embeddings.json

## 5. Chat with the PDF

```markdown
## Ask Questions

Run:

```bash
python3 chat.py

Example:

Ask a question:
What are queries, keys and values?
```


---

## 6. How It Works

```markdown
## Architecture

PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
JSON Storage
↓
Question Embedding
↓
Cosine Similarity Search
↓
Top-K Chunks
↓
Prompt Construction
↓
Gemini Answer
```

## 7. Using Your Own PDF

You can use any PDF document with this project.

1. Copy your PDF into:

```text
data/docs/
```

Example:

```text
data/docs/my_document.pdf
```

2. Update the filename in `index.py`:

```python
full_text = load_pdf("my_document.pdf")
```

3. Rebuild the index:

```bash
python3 index.py
```

This will:

* Load the new PDF
* Create chunks
* Generate embeddings
* Overwrite `data/embeddings.json`

4. Start chatting with your document:

```bash
python3 chat.py
```
