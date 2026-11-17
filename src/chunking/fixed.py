from bs4 import BeautifulSoup
from transformers import AutoTokenizer

MODEL_NAME = "BAAI/bge-small-en-v1.5"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(" ", strip=True)

def chunk_text(text, chunk_size=256, overlap=32):
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    encoding = tokenizer(
        text,
        add_special_tokens=False,
        return_offsets_mapping=True
    )

    token_ids = encoding["input_ids"]
    offsets = encoding["offset_mapping"]

    chunks = []
    start_token = 0

    while start_token < len(token_ids):
        end_token = min(start_token + chunk_size, len(token_ids))

        char_start = offsets[start_token][0]
        char_end = offsets[end_token - 1][1]

        chunk_text_value = text[char_start:char_end]

        chunks.append({
            "text": chunk_text_value,
            "start": char_start,
            "end": char_end,
            "start_token": start_token,
            "end_token": end_token
        })

        if end_token == len(token_ids):
            break

        start_token = end_token - overlap

    return chunks


if __name__ == "__main__":
    from pathlib import Path

    input_path = Path("data/processed/path_params.html")
    html = input_path.read_text(encoding="utf-8")

    text = extract_text_from_html(html)

    chunks = chunk_text(
        text,
        chunk_size=256,
        overlap=32
    )

    print(f"Created {len(chunks)} chunks")

    for i, chunk in enumerate(chunks[:3], start=1):
        print(f"\nChunk {i}")
        print(f"Token range: {chunk['start_token']}-{chunk['end_token']}")
        print(f"Character range: {chunk['start']}-{chunk['end']}")
        print(chunk["text"][:300])