from recsystools.utils import math


def test_add():
    assert math.add(1, 5) == 6
    assert math.add(-1, 45) == 44
