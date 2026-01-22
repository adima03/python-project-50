check:
	uv run ruff check

install:
	uv sync 

build:
	uv build

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest

