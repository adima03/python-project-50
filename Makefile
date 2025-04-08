check:
	uv run ruff check

install:
	uv sync 

build:
	uv build

package-install:
	uv tool install dist/*.whl

make tests:
	uv run pytest

