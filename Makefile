check:
	uv run ruff check
	uv run pytest

install:
	uv sync 

build:
	uv build

package-install:
	uv tool install dist/*.whl

