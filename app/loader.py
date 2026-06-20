import pypdf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_pdf(filename: str) -> str:
    # reader = pypdf.PdfReader(path)
    # full_string = "\n".join([page.extract_text() or "" for page in reader.pages])
    # return full_string

    # using the below way so I know where page content ends or start,useful later for debugging
    pdf_path = BASE_DIR / "data/docs" / filename
    reader = pypdf.PdfReader(str(pdf_path))

    full_string = ""

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        full_string += f"\n\n--- PAGE {i+1} ----\n\n{text}"
    return full_string