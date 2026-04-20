# Agent Guidelines

## Package Management

- Use `uv` as the Python package manager and runtime.
  - Run scripts/tools via `uv run <tool>` (e.g. `uv run pytest`, `uv run ruff check`).
  - Add dependencies with `uv add`; sync the environment with `uv sync`.
  - Never use `pip` directly.

## Code Style

- Follow ruff standards. Before committing, always run:
  ```
  uv run ruff check --fix .
  uv run ruff format .
  ```
- Line length: **120 characters**.
- Enabled ruff rule-sets: `B`, `D`, `C4`, `S`, `F`, `E`, `W`, `UP`, `I`, `RUF`.
- Ignored rules: `D203`, `D212`, `D100`, `D104`, `D107`, `D401` — use D211 / D213 docstring style.
- Test files (`tests/**`) may omit docstrings and use `assert` freely (`S101` ignored there).

## Code Optimization

- Prefer modern Python 3.13+ features and idioms.
- Avoid unnecessary imports, variables, or functions.
- Suggest more efficient algorithms or data structures when applicable.
- Find common patterns and abstract them into reusable functions or classes (adhering the DRY principle).

## Type Annotations

- Add type hints to all function signatures and variables where inferable.
- Verify with `uv run mypy`; the project enforces `disallow_untyped_defs = true`.

## Docstrings

- Add Google-style docstrings to all public functions, methods, and classes.
- Module-level and `__init__` docstrings are optional (D100, D104, D107 are ignored).

## Python Version

- Target **Python 3.13**; prefer modern syntax and stdlib features:
  - `match` / `case` for structural pattern matching.
  - `X | Y` union types instead of `Optional[X]` or `Union[X, Y]`.
  - `tomllib`, `pathlib`, `typing.Self`, etc.

## Project Structure

- Source code lives under `src/<package_name>/` (src layout).
- Tests live under `tests/`; the package is importable after `uv sync`.
- Do not place importable source files at the project root.

## Django Templates / UI

- Follow Django template best practices.
- Use `{% block %}` and `{% extends %}` for template inheritance.
- Avoid logic in templates; use template tags and filters instead.
- Always add the block name at the end of the block comment for clarity, e.g. `{% endblock content %}`.
- Prefer the new django 6 partials syntax for reusable template components.
- Design mobile-first and ensure templates are responsive, using Tailwind CSS / DaisyUI for styling.

## Views and Forms

- Use class-based views (CBVs) for better organization and reusability.
- For forms, prefer Django's built-in form classes and validation mechanisms.
- Use htmx for dynamic interactions where appropriate, following best practices for progressive enhancement and accessibility.

## Testing

- Use `pytest` for all tests; run via `uv run pytest`.
- Maintain or improve coverage (reported to `term-missing` and `xml`).
- When adding features, add corresponding tests in `tests/`.

## Commit Messages

- Follow **Conventional Commits** format (enforced by commitlint):
  ```
  <type>(<scope>): <short summary>
  ```
  Common types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `build`.
- Commits of type `chore`, `ci`, `refactor`, `style`, `test` are excluded from the changelog.
