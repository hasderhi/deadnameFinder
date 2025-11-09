# GitHub Repository Deadname Indexer

A small Python utility that automatically scans all your GitHub repositories for unwanted occurrences of specific terms (such as your old name), indexes where they appear, and saves the results for easy cleanup. You can obviously use this for everything, not just your deadname. I just happened to have that specific use case.

---

##  Features
- Clones repositories listed in `repos.txt` (one repo URL per line)
- Searches every file for a given keyword or phrase
- Creates a detailed JSON index with all matches (`index.json`)
- Groups results by repository, file, and line (`index_grouped.json`)
- Automatically deletes cloned repositories after scanning

---

##  Requirements
- Python 3.8 or newer  
- `git` installed and available in your system PATH  
- A valid GitHub **Personal Access Token (PAT)** 

---

## Author

**Annabeth Kisling**

Created to make changing your name a bit easier, at least on GitHub 🏳️‍⚧️.

[annabeth@tk-dev-software.com](annabeth@tk-dev-software.com)
