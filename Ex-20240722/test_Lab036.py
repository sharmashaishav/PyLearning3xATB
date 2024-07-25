import pytest

@pytest.mark.smoke
def test_addition():
    assert (2+2 == 4)

@pytest.mark.regression
def test_subtraction():
    assert 4-2 == 2

@pytest.mark.skip(reason='not working')
def test_sub():
    assert 4+4==1