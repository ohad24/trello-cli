import toml
from trellocli import __version__


def test_main():
    with open("pyproject.toml", "r") as f:
        data = toml.load(f)
        poetry_version = data["tool"]["poetry"]["version"]
    assert poetry_version == __version__
