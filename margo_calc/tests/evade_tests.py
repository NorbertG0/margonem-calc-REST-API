from services.evade import *
import pytest

def test_calculate_evade():
    assert calculate_evade(1, 1) == 20
    assert calculate_evade(1, 299) == pytest.approx(0.0668896)
    assert calculate_evade(1, 300) == pytest.approx(0.06666666)
    assert calculate_evade(1, 301) == pytest.approx(0.06666666)

    assert calculate_evade(100, 1) == 2000
    assert calculate_evade(100, 299) == pytest.approx(6.6889632)
    assert calculate_evade(100, 300) == pytest.approx(6.6666666)
    assert calculate_evade(100, 301) == pytest.approx(6.6666666)