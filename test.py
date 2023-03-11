from github import Github
from faker import Faker

faker = Faker()


# Replace with your personal access token and repository name
ACCESS_TOKEN = "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"
REPO_NAME = "Cmatrix1/Github-FC"

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)


def update_file(file_path, commit_message, new_content):
    try:
        contents = repo.get_contents(file_path, ref="main")
        last_content = open(file_path, "r").read()
        repo.update_file(
            path=file_path,
            message=commit_message,
            content=last_content+"\n"+new_content,
            sha=contents.sha,
            branch="main"
        )
        print(f"Successfully updated {file_path}!")
    except Exception as e:
        print(f"An error occurred: {e}")




for _ in range(20):
    # Get the latest commit on the main branch
    branch = repo.get_branch("main")
    latest_commit_sha = branch.commit.sha

    # Update the contents of the file
    file_path = "file-01.txt"
    new_content = faker.text()
    commit_message = "Update file via API the random text:" + new_content[:10]

    update_file(file_path, commit_message, new_content)