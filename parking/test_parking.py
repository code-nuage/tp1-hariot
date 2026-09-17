import pytest
from parking import final_price

# --+ E1 +--
@pytest.mark.parametrize("minutes", [0, 10, 29, 30])
def test_thirty_or_less_minutes_parking_is_free(minutes):
    assert final_price(minutes) == 0

# --+ E2 +--
def test_thirty_one_minutes_is_paid_once():
    assert final_price(31) == 1.50

def test_an_hour_and_a_minute_is_paid_twice():
    assert final_price(61) == 3.00

@pytest.mark.parametrize("minutes, expected", [(90, 3), (120, 4.5), (150, 6.00), (151, 7.50)])
def test_each_half_hour_get_its_price(minutes, expected):
    assert final_price(minutes) == expected
