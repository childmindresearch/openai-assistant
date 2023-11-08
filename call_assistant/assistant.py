import pathlib

import openai
import pydantic


def run_prompt(
    *,
    assistant_id: str,
    max_wait: float,
    prompt: str,
    files: list[pathlib.Path],
    api_key: pydantic.SecretStr,
):
    """Runs a prompt with an OpenAI Assistant.

    Args:
        assistant_id: The ID of the Assistant to use.
        max_wait: The maximum time to wait for a response.
        prompt: The prompt to use.
        files: A list of files to upload.
        api_key: The API key to use.

    """

    client = openai.OpenAI(api_key.get_secret_value())

    assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)
    thread = client.beta.threads.create()
    openai_files = [client.files.create(file=open(file, "rb")) for file in files]
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt,
        file_ids=[file.id for file in openai_files],
    )
    run = client.beta.threads.runs.create(thread.id, assistant.id)
    run = client.beta.threads.runs.retrieve(
        thread.id, assistant.id, run.id, timeout=max_wait
    )

    for file in openai_files:
        client.beta.assistants.files.delete(assistant_id=assistant.id, file_id=file.id)
