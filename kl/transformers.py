from __future__ import unicode_literals

from .data import command_keys_repr, layout_agnostic_keys, spanish_layout


def _only_shifts(modifiers):
    """Check if modifiers pressed are only shifts"""
    if not modifiers or len(modifiers) > 2:
        return False
    if len(modifiers) == 2:
        return 'left shift' in modifiers and 'right shift' in modifiers
    if len(modifiers) == 1:
        return 'left shift' in modifiers or 'right shift' in modifiers


def _only_right_alt(modifiers):
    """Check if the only modifier pressed is right alt"""
    if not modifiers or len(modifiers) > 1:
        return False
    return 'right alt' in modifiers


def english_usa(keys):
    """Apply English (USA) layout to the pressed keys"""
    pass


def spanish(keys):
    """Apply Spanish layout to the pressed keys"""
    key = keys['regular'][0]
    modifiers = keys['modifiers']

    try:
        if not modifiers:
            if key in layout_agnostic_keys.keys():
                res = layout_agnostic_keys[key]
            elif key in command_keys_repr.keys():
                res = command_keys_repr[key]
            else:
                res = spanish_layout['wo_mods'][key]
        elif _only_shifts(modifiers):
            res = spanish_layout['shift'][key]
        elif _only_right_alt(modifiers):
            res = spanish_layout['right_alt'][key]
        else:
            res = None
    except KeyError:
        res = None

    return res
