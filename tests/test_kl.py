import pytest
from kl import kl


def test_get_keys_empty_keymap():
    keymap = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert kl.get_keys(keymap) == dict(modifiers=[], regular=[])


def test_get_keys_keymap_with_modifiers_and_regular_keys():
    keymap = [0, 0, 0, 0, 32, 1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    regular = ['d']
    modifiers = ['left ctrl', 'left shift']
    assert kl.get_keys(keymap) == dict(modifiers=modifiers, regular=regular)
