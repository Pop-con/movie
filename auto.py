import os
from git import Repo
from github import Github

# Define your local repository path and GitHub credentials
repo_dir = '/path/to/your/local/repo'  # Update this with the local repository path
github_token = 'your_github_token'  # Replace this with your GitHub token
github_repo_name = 'Pop-con/movie'  # Replace this with your GitHub username and repository name

# Initialize the local repository
repo = Repo(repo_dir)

# Authenticate with GitHub
g = Github(github_token)
github_repo = g.get_repo(github_repo_name)

def commit_and_push_changes():
    # Check if there are changes to commit
    if repo.is_dirty(untracked_files=True):
        repo.git.add(A=True)
        repo.index.commit("Automatic commit message")
        origin = repo.remote(name='origin')
        origin.push()

# Schedule the function to run every X minutes (you can change the interval)
import time

while True:
    commit_and_push_changes()
    time.sleep(600)  # Sleep for 10 minutes
