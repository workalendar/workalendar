import sys

if sys.version_info[:2] < (3, 8):  # coverage: exclude
    import importlib_metadata
else:  # coverage: exclude
    import importlib.metadata as importlib_metadata

try:
    #: Module version, as defined in PEP-0396.
    __version__ = importlib_metadata.version(__name__)
except importlib_metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
