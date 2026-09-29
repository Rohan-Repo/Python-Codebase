import csv
import json
from pathlib import Path

# Ask for the CSV file path and remove accidental quotes.
source_csv = Path(
    input("Enter the source CSV file path: ").strip().strip('"').strip("'")
).expanduser()

# Validate that the selected file exists and is a CSV.
if not source_csv.is_file() or source_csv.suffix.lower() != ".csv":
    raise SystemExit(f"Invalid or missing CSV file: {source_csv}")

# Create the JSON output in the same folder with the same base name.
destination_json = source_csv.with_suffix(".json")

# Use utf-8-sig to remove a potential BOM from the first CSV header.
with source_csv.open("r", newline="", encoding="utf-8-sig") as csv_file:
    records = list(csv.DictReader(csv_file))

# Create readable, UTF-8 JSON.
with destination_json.open("w", encoding="utf-8") as json_file:
    json.dump(records, json_file, indent=4, ensure_ascii=False)

print(f"JSON file created: {destination_json}")
print(f"Records exported: {len(records)}")