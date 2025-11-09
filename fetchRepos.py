import requests

USERNAME = "your-github-username"
TOKEN = "your-personal-access-token"

url = f"https://api.github.com/user/repos"
params = {"per_page": 100, "page": 1, "type": "all"}
headers = {"Authorization": f"token {TOKEN}"}

all_repos = []

print(f"Fetching repositories for {USERNAME}...")

while True:
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"GitHub API error: {response.status_code} - {response.text}")
        break

    repos = response.json()
    if not repos:
        break

    for repo in repos:
        all_repos.append(repo["clone_url"])

    params["page"] += 1

with open("repos.txt", "w", encoding="utf-8") as f:
    for repo_url in all_repos:
        f.write(repo_url + "\n")

print(f"Found {len(all_repos)} repositories.")
print("Saved to repos.txt")
