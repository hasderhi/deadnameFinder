import os
import subprocess
import json
import re
import tempfile
from pathlib import Path

# === CONFIG ===
KEYWORDS = ["YourOldNameHere"]  # Put your deadname(s) here
REPOS_FILE = "repos.txt"
OUTPUT_FILE = "index.json"

# ===============================

def clone_repo(url, dest_dir):
    """Clone a GitHub repo to a temp directory."""
    subprocess.run(["git", "clone", "--depth", "1", url, dest_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def search_in_repo(repo_path, repo_url):
    """Search for the keyword(s) in all files."""
    results = []
    for root, _, files in os.walk(repo_path):
        for f in files:
            path = Path(root) / f
            try:
                text = path.read_text(errors="ignore")
            except Exception:
                continue

            for keyword in KEYWORDS:
                for i, line in enumerate(text.splitlines(), 1):
                    if keyword.lower() in line.lower():
                        # Construct GitHub link
                        rel_path = path.relative_to(repo_path)
                        repo_name = repo_url.split("/")[-1].replace(".git", "")
                        github_link = f"{repo_url.replace('.git', '')}/blob/main/{rel_path}#L{i}"

                        results.append({
                            "repo": repo_name,
                            "repo_url": repo_url,
                            "file": str(rel_path),
                            "line_number": i,
                            "line": line.strip(),
                            "github_link": github_link
                        })
    return results

def main():
    if not os.path.exists(REPOS_FILE):
        print("repos.txt not found.")
        return

    all_results = []
    with open(REPOS_FILE, "r", encoding="utf-8") as f:
        repos = [r.strip() for r in f if r.strip()]

    for repo in repos:
        with tempfile.TemporaryDirectory() as tmpdir:
            print(f"Processing {repo}...")
            try:
                clone_repo(repo, tmpdir)
                matches = search_in_repo(tmpdir, repo)
                all_results.extend(matches)
            except Exception as e:
                print(f"Error processing {repo}: {e}")

    # Write all results to JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"Done! Indexed {len(all_results)} matches. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
