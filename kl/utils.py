from __future__ import unicode_literals


digits = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyz'


def only_shifts(modifiers):
    """Check if modifiers pressed are only shifts"""
    if not modifiers or len(modifiers) > 2:
        return False
    if len(modifiers) == 2:
        return 'left shift' in modifiers and 'right shift' in modifiers
    if len(modifiers) == 1:
        return 'left shift' in modifiers or 'right shift' in modifiers


def only_right_alt(modifiers):
    """Check if the only modifier pressed is right alt"""
    if not modifiers or len(modifiers) > 1:
        return False
    return 'right alt' in modifiers
