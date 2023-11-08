"""Module for parsing command line arguments."""
import argparse

import pydantic


def parse_args():
    """Parse command line arguments for calling an OpenAI Assistant.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Call an OpenAI Assistant")
    parser.add_argument("assistant_id", type=str, help="Assistant ID")
    parser.add_argument("prompt", type=str, help="Prompt")
    parser.add_argument("api_key", type=pydantic.SecretStr, help="API Key")
    parser.add_argument(
        "max_wait", type=int, help="Maximum time to wait for a response."
    )

    return parser.parse_args()
