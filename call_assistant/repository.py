"""Contains functions for working with the repository."""
import os
import pathlib
import zipfile

import github


def zip_repository(output_file: pathlib.Path) -> None:
    """Compresses the entire contents of the workspace directory into a zip file.

    Args:
        output_file: The path to the output zip file.

    """
    workspace = pathlib.Path("/github/workspace")

    with zipfile.ZipFile(output_file, "w") as zip:
        for file in workspace.glob("**/*"):
            zip.write(file)


def comment_on_pull_request(message: str) -> None:
    """Comments on the current pull request.

    Args:
        message: The message to post.

    """
    github_token = os.environ["GITHUB_TOKEN"]
    github_repository = os.environ["GITHUB_REPOSITORY"]
    github_pr_number = os.environ["GITHUB_PR_NUMBER"]

    client = github.Github(github_token)
    repository = client.get_repo(github_repository)
    pull_request = repository.get_pull(github_pr_number)
    pull_request.create_comment(message)


def is_pull_request() -> bool:
    """Returns True if the current workflow run is a pull request.

    Returns:
        bool: True if the current workflow run is a pull request.

    """
    return os.environ.get("GITHUB_EVENT_NAME") == "pull_request"
