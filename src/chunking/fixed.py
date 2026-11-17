import json
from pathlib import Path

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
    processed_dir = Path("data/processed")
    output_path = Path("data/chunks/fixed_chunks.jsonl")

    all_chunks = []

    for input_path in processed_dir.glob("*.html"):
        html = input_path.read_text(encoding="utf-8")
        text = extract_text_from_html(html)

        chunks = chunk_text(
            text,
            chunk_size=256,
            overlap=32
        )

        for chunk_id, chunk in enumerate(chunks):
            chunk["source"] = input_path.name
            chunk["chunk_id"] = f"{input_path.stem}_{chunk_id}"
            all_chunks.append(chunk)

        print(f"{input_path.name}: {len(chunks)} chunks")

    with output_path.open("w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk) + "\n")

    print(f"\nSaved {len(all_chunks)} chunks to {output_path}")