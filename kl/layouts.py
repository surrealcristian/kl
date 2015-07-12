# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .data import command_keys
from .utils import digits, letters, only_shifts, only_right_alt

english_layout = {
    'no_mods': {},
    'shift': {},
    'right_alt': {},
}

spanish_layout = {
    'no_mods': {
        ';': 'ñ',
        '`': 'º',
        '-': '\'',
        '=': '¡',
        '<': '<',
        '[': '`',
        ']': '+',
        '\'': '´',
        '\\': 'ç',
        ',': ',',
        '.': '.',
        '/': '-',
    },
    'shift': {
        ';': 'Ñ',
        '0': '=',
        '1': '!',
        '2': '"',
        '3': '·',
        '4': '$',
        '5': '%',
        '6': '&',
        '7': '/',
        '8': '(',
        '9': ')',
        '`': '~',
        '-': '?',
        '=': '¿',
        '<': '>',
        '[': '^',
        ']': '*',
        '\'': '¨',
        '\\': 'Ç',
        ',': ';',
        '.': ':',
        '/': '_',
        'keypad /': '<keypad />',
        'keypad *': '<keypad *>',
        'keypad intro': '<keypad intro>',
    },
    'right_alt': {
        'q': '@',
        '0': '}',
        '1': '|',
        '2': '@',
        '3': '#',
        '4': '~',
        '5': '½',
        '6': '¬',
        '7': '{',
        '8': '[',
        '9': ']',
        '`': '\\',
        '-': '\\',
        '=': '~',
        '<': '|',
        '[': '[',
        ']': ']',
        '\'': '{',
        '\\': '}',
        '.': '·',
    },
}


def english_usa(keys):
    """Apply English (USA) layout to the pressed keys"""
    pass


def spanish(keys):
    """Apply Spanish layout to the pressed keys"""
    key = keys['regular'][0]
    modifiers = keys['modifiers']

    try:
        if not modifiers:
            if key in letters or key in digits:
                res = key
            elif key in command_keys:
                res = '<' + key + '>'
            else:
                res = spanish_layout['no_mods'][key]
        elif only_shifts(modifiers):
            if key in letters:
                res = key.upper()
            else:
                res = spanish_layout['shift'][key]
        elif only_right_alt(modifiers):
            res = spanish_layout['right_alt'][key]
        else:
            res = None
    except KeyError:
        res = None

    return res
