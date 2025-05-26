import csv
import os

def write_csv_row(file_path, row_name, data):
    fieldnames = ["frame"]
    existing_rows = []
    file_exists = os.path.exists(file_path)

    if file_exists:
        with open(file_path, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames or ["row"]
            existing_rows = list(reader)

    # determine if we need to add new columns
    new_fields = [key for key in data if key not in fieldnames]
    if new_fields:
        fieldnames += new_fields

        # init fields to 0
        for row in existing_rows:
            for field in new_fields:
                row[field] = "0"

        # create new row
        new_row = {key: "0" for key in fieldnames}
        new_row["row"] = row_name
        for key, value in data.items():
            new_row[key] = value if value is not None else "0"
        existing_rows.append(new_row)

        # rewrite entire file :/ awkward
        with open(file_path, mode="w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(existing_rows)

    else:
        # just append a row
        with open(file_path, mode="a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            new_row = {key: "0" for key in fieldnames}
            new_row["row"] = row_name
            for key, value in data.items():
                new_row[key] = value if value is not None else "0"
            writer.writerow(new_row)

def count_strings(lst):
    counts = {}
    for s in lst:
        counts[s] = counts.get(s, 0) + 1
    return counts
