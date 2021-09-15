try:
    import skyfield  # noqa: F401
    import skyfield_data  # noqa: F401
    from .skyfield_astronomy import calculate_equinoxes, solar_term
except ImportError:
    from .precomputed_astronomy import calculate_equinoxes, solar_term

__all__ = [
    'calculate_equinoxes',
    'solar_term',
]
