import csv
import json
from pathlib import Path

# Pathlib works cleanly on Windows, macOS, and Linux.
input_file = Path("data") / "AD-User-Info.csv"
output_file = Path("data") / "AD-User-Info.json"

# ── Read the CSV file ────────────────────────────────────────
# Use utf-8-sig to remove a possible UTF-8 BOM from the first CSV header.
# newline="" is recommended when using Python's csv module.
# encoding="utf-8-sig" removes a possible UTF-8 BOM from the
# beginning of the file, preventing corruption of the "Name" header.

with input_file.open("r", newline="", encoding="utf-8-sig") as src_csv:
    rows = list(csv.DictReader(src_csv))
# DictReader uses the CSV header row as dictionary keys.
# Convert the DictReader iterator into a list so it can be written as a JSON array.
    

# ── Write the data to a formatted JSON file ──────────────────
# Create readable UTF-8 JSON.
# indent=4 makes the JSON easy for humans to read.
# ensure_ascii=False writes normal Unicode characters directly
# instead of escaping them as \uXXXX sequences.
with output_file.open("w", encoding="utf-8") as dest_json:
    json.dump(rows, dest_json, indent=4, ensure_ascii=False)

# Reopen the JSON file to verify that it was successfully created
with output_file.open( mode="r", encoding="utf-8") as json_file:
    file_data = json.load(json_file)
    print(json.dumps(file_data, indent=4, ensure_ascii=False))

print(f"Formatted JSON file created successfully: {output_file}")