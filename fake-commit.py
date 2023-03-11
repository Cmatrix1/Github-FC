
import os
from github import Github

# Set up GitHub credentials
username = 'Cmatrix1'
email = 'Sadeghmajidi980@gmail.com'
password = 'joz1396sadegh1384'

# Create a GitHub instance using credentials
g = Github("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")

# Get the specified repository
repo_name = "Github-FC"
repo = g.get_user().get_repo(repo_name)

# Set the directory containing the files to modify
dir_path = "."

# Set the text to add to the files
new_text = '# This text was added by a Python script!'


# Loop through each file in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.txt'): # Modify only .txt files
        # Read the contents of the file
        with open(os.path.join(dir_path, filename), 'r+') as f:
            contents = f.read()

            # Add the new text to the file contents
            contents += '\n' + new_text

            # Move the file pointer to the beginning of the file
            f.seek(0)

            # Write the modified contents back to the file
            f.write(contents)

            # Truncate any remaining content after the end of the new content
            f.truncate()

        # Add, commit, and push the modified file to the repository
        commit_message = f"Modified {filename} via Python script"
        print(filename)

        branch = repo.get_branch('main')
        latest_commit_sha = branch.commit.sha
        repo.create_file(filename, commit_message, contents, branch='main', sha=latest_commit_sha)
        # repo.create_file()

