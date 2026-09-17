import pytest
from parking import final_price

@pytest.mark.parametrize("minutes", [0, 10, 29, 30])
def test_thirty_or_less_minutes_parking_is_free(minutes):
    assert final_price(minutes) == 0
