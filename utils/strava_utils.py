# src/strava_utils.py
def mps_to_kmh(mps: float) -> float:
    """
    Convert meters/second to km/h.
    Example: 10.0 m/s -> 36.0 km/h
    """
    return mps * 3.6