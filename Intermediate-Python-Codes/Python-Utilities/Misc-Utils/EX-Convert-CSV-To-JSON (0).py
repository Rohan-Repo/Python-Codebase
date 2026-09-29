# ============================================================
# CSV to JSON Converter
#
# Prompts the user for a source CSV file, reads its rows,
# and creates a formatted JSON file in the same folder.
#
# Handles CSV files that contain a UTF-8 Byte Order Mark (BOM)
# by using encoding="utf-8-sig".
# ============================================================

import csv
import json
from pathlib import Path


# ── Step 1: Ask the user for the source CSV file ─────────────
# Example input:
# C:\Users\YourName\Documents\AD-User-Info.csv
# or:
# data/AD-User-Info.csv
source_csv_input = input(
    "Enter the full path or relative path of the source CSV file: "
).strip()


# ── Step 2: Remove quotes from pasted or drag-and-dropped paths ─
# If the user pastes a path with quotes, remove them.
# Example:
# "C:\Users\YourName\Documents\AD-User-Info.csv"
# becomes:
# C:\Users\YourName\Documents\AD-User-Info.csv
source_csv_input = source_csv_input.strip('"').strip("'")


# ── Step 3: Convert the input text into a Path object ───────
source_csv_path = Path(source_csv_input).expanduser()


# ── Step 4: Validate the source file ─────────────────────────
# Check whether the entered file exists.
if not source_csv_path.exists():
    print(f"\nERROR: CSV file was not found:\n{source_csv_path}")
    raise SystemExit(1)

# Ensure the entered item is actually a file, not a directory.
if not source_csv_path.is_file():
    print(f"\nERROR: The path is not a file:\n{source_csv_path}")
    raise SystemExit(1)

# Confirm that the selected file has the expected extension.
if source_csv_path.suffix.lower() != ".csv":
    print(f"\nERROR: Please select a CSV file. Selected: {source_csv_path.name}")
    raise SystemExit(1)


# ── Step 5: Create the JSON output filename ──────────────────
# If input is:
# AD-User-Info.csv
#
# Output becomes:
# AD-User-Info.json
destination_json_path = source_csv_path.with_suffix(".json")


# ── Step 6: Read the CSV data ────────────────────────────────
try:
    # utf-8-sig removes a UTF-8 BOM if one exists.
    # This prevents a broken first header like "\ufeffName".
    #
    # newline="" is recommended when reading CSV files in Python.
    with source_csv_path.open(
        mode="r",
        newline="",
        encoding="utf-8-sig"
    ) as source_csv_file:

        # DictReader converts each CSV row into a dictionary.
        # The CSV header becomes the JSON property names.
        #
        # Example:
        # Name,UserName,EmailID
        #
        # becomes:
        # {
        #     "Name": "Phoebe Pamela Buffay",
        #     "UserName": "phoebe.buffay",
        #     "EmailID": "phoebe.buffay@easysystems.in"
        # }
        csv_reader = csv.DictReader(source_csv_file)

        # Convert the reader iterator to a list so it can be
        # exported as a JSON array.
        records = list(csv_reader)

except UnicodeDecodeError:
    print(
        "\nERROR: The CSV file could not be read as UTF-8.\n"
        "Try saving the source CSV as UTF-8, then run the script again."
    )
    raise SystemExit(1)

except csv.Error as error:
    print(f"\nERROR: The CSV file could not be processed: {error}")
    raise SystemExit(1)


# ── Step 7: Validate that a header row was found ──────────────
if not records:
    print(
        "\nWARNING: The CSV file contains no data rows.\n"
        "An empty JSON array will be created."
    )


# ── Step 8: Write formatted JSON ─────────────────────────────
try:
    with destination_json_path.open(
        mode="w",
        encoding="utf-8"
    ) as destination_json_file:

        # indent=4 formats the JSON for readability.
        #
        # ensure_ascii=False keeps Unicode characters readable.
        # For example, "José" remains "José" rather than "\u00e9".
        json.dump(
            records,
            destination_json_file,
            indent=4,
            ensure_ascii=False
        )

except OSError as error:
    print(f"\nERROR: Could not create JSON file: {error}")
    raise SystemExit(1)


# ── Step 9: Display a completion summary ─────────────────────
print("\n========================================")
print(" CSV to JSON conversion completed")
print("========================================")
print(f" Source CSV       : {source_csv_path}")
print(f" Destination JSON : {destination_json_path}")
print(f" Records exported : {len(records)}")
print("========================================")