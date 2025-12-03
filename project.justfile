## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Run Python tests and report test coverage
[group('special dcat-ap-plus model')]
coverage:
  uv run python -m coverage run -m pytest
  uv run python -m coverage html
