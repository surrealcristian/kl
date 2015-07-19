import pytest
from kl import utils


def test_only_shifts():
    assert utils.only_shifts([]) == False
    assert utils.only_shifts(['left ctrl']) == False
    assert utils.only_shifts(['left ctrl', 'right shift']) == False
    assert utils.only_shifts(['right shift', 'left shift']) == True
    assert utils.only_shifts(['right shift']) == True


def test_only_right_alt():
    assert utils.only_right_alt([]) == False
    assert utils.only_right_alt(['right shift']) == False
    assert utils.only_right_alt(['right alt']) == True
