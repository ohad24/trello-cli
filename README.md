# Trello CLI

CLI tool for Trello.

## Basic usage

```bash
# with `__main__.py` file.  
python trellocli_ohad24 get-lists NLelg4Zf
# specific file
python trellocli_ohad24/TrelloCLI.py get-lists NLelg4Zf
# build package
poetry build
# install package from wheel file.  
pip install ~/projects/trello-cli/dist/trellocli_ohad24-0.0.3-py3-none-any.whl --upgrade --force-reinstall

# test
poetry run pytest tests/

# use
tcli get-lists NLelg4Zf
# or in development mode
poetry run tcli get-lists NLelg4Zf

# publish to test-PyPI
poetry publish -r test-pypi

# install from pypi
pip install --index-url https://test.pypi.org/simple/ trellocli2 --extra-index-url https://pypi.org/simple trellocli2
```

### Publish

<https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org>  
I've successfully used tokens and poetry to upload to PyPI and TestPyPI. I believe you just need to change the TestPyPI URL you are configuring by appending /legacy/:

`poetry config repositories.test-pypi https://test.pypi.org/legacy/`

You can then create your token as you were doing previously:

`poetry config pypi-token.test-pypi <your-token>`

## Docs

- [Fire](https://github.com/google/python-fire/blob/master/docs/guide.md)
- [Pydantic](https://pydantic-docs.helpmanual.io/en/latest/)
- [Trello](https://trello.com/docs/api/reference/)
- [Tabulate](https://github.com/astanin/python-tabulate/blob/master/README.md)
- [Poery](https://python-poetry.org/docs/)
