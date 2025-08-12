from strava_utils import mps_to_kmh

def test_mps_to_kmh_basic():
    assert mps_to_kmh(10.0) == 36.0

def test_mps_to_kmh_zero():
    assert mps_to_kmh(0.0) == 0.0

def test_mps_to_kmh_float_precision():
    # 2.78 m/s is ~10.008 km/h
    assert math.isclose(mps_to_kmh(2.78), 10.008, rel_tol=0, abs_tol=1e-6)
