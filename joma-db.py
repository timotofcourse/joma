import requests
import json
import sqlite3

repo_file_path = "joma-repos.json"
file_extension = "py"
pat = "YOUR_PAT_HERE"
api_endpoint = "https://api.github.com"
headers = {"Authorization": f"Bearer {pat}"}

# Load the repository list from the JSON file

with open(repo_file_path, "r") as f:
    repos = json.load(f)


conn = sqlite3.connect("files.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS files (name TEXT, url TEXT)")

# Loop through the repositories and send a GET request to the search endpoint to find the files

for repo in repos:
    owner = repo["owner"]
    name = repo["name"]
    search_url = f"{api_endpoint}/search/code?q=repo:{owner}/{name}+extension:{file_extension}"
    response = requests.get(search_url, headers=headers)
    results = json.loads(response.content.decode("utf-8"))
    if results["total_count"] > 0:
        for item in results["items"]:
            file_name = item["name"]
            file_url = item["html_url"]
            print(f"Found file '{file_name}' in repository '{owner}/{name}'")
            c.execute("INSERT INTO files (name, url) VALUES (?, ?)", (file_name, file_url))
    else:
        print(f"No files found with the extension '{file_extension}' in the '{owner}/{name}' repository.")


conn.commit()
conn.close()
