from ev.bill import Ev_Saving
import pytest

ev = Ev_Saving()

def test_electric_bill():
    actual = ev.electic_bill('y',300)
    expected = 15.00
    assert actual == expected
def test_electric_bill2():
    actual = ev.electic_bill('n',300)
    expected = 36.00
    assert actual == expected

def test_increased_electricity():
    actual = ev.increased_electricity(200)
    expected = 40.00
    assert actual == expected

