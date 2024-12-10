poetry run python lingua/cli.py --utc -5
poetry run pytest

poetry update --dry-run

poetry update

poetry build
pip3 install *.whl

tag using git for versioning