import pytest
from kl import kl


def test_get_keys_empty_keymap():
    keymap = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert kl.get_keys(keymap) == dict(modifiers=[], regular=[])


def test_get_keys_keymap_with_one_regular_keys():
    keymap = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert kl.get_keys(keymap) == dict(modifiers=[], regular=['q'])
