try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata


#: Module version, as defined in PEP-0396.
__version__ = metadata.version(__package__)
