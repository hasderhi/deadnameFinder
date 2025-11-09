import json
from collections import defaultdict

INPUT_FILE = "index.json"
OUTPUT_FILE = "index_grouped.json"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    grouped = defaultdict(lambda: defaultdict(list))

    for entry in data:
        repo = entry["repo"]
        file = entry["file"]
        line_number = entry["line_number"]
        grouped[repo][file].append(line_number)

    # Sort and pretty-format
    grouped_sorted = {
        repo: {f: sorted(lines) for f, lines in files.items()}
        for repo, files in sorted(grouped.items())
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(grouped_sorted, f, indent=2, ensure_ascii=False)

    print(f"Grouped index saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
