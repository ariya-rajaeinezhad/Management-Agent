import os


def load_prompt(filename: str) -> str:
    """
    Loads a prompt template from the prompts/ directory.
    Uses the directory relative to this file's location.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, "prompts", filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Prompt file not found at: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()