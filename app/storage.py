#Since I call this fn in index.py
#before calling I will be storing chunks from chunker.py and then alse the embedings in a list of dicts and chunk_ids in records variable in index.py
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

fp = BASE_DIR / "data" / "embeddings.json"

#this function stores the chunks and embeddings of the file in a json file, so we dont have to run it every time a user asks a query
def save_records(records:list[dict]) -> None:
    with open(fp, "w") as f:
        json.dump(records,f, indent=4)


# this function is, when we restart the program to load the python objects back in memory, reads json file and converts it to python objects
def load_records() -> list[dict]:
    with open(fp, "r") as f:
        return json.load(f)