import pathlib

from call_assistant import assistant, cli, repository

if not repository.is_pull_request():
    raise RuntimeError("This action can only be run on pull requests.")

args = cli.parse_args()
repository_file = pathlib.Path("/github/workspace/repo.zip")
repository.zip_repository(repository_file)

messages = assistant.run_prompt(
    assistant_id=args.assistant_id,
    max_wait=args.max_wait,
    prompt=args.prompt,
    files=[repository_file],
    api_key=args.api_key,
)
