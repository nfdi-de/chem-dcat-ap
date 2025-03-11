from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package not installed
    # poetry-dynamic-versioning will insert here the correct version on build
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
