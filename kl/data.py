# -*- coding: utf-8 -*-

from __future__ import unicode_literals

keymap_values_list = {
    1: {
        2: 'esc',
        4: '1',
        8: '2',
        16: '3',
        32: '4',
        64: '5',
        128: '6',
    },
    2: {
        1: '7',
        2: '8',
        4: '9',
        8: '0',
        16: '-',
        32: '=',
        64: 'backspace',
        128: 'tab',
    },
    3: {
        1: 'q',
        2: 'w',
        4: 'e',
        8: 'r',
        16: 't',
        32: 'y',
        64: 'u',
        128: 'i',
    },
    4: {
        1: 'o',
        2: 'p',
        4: '[',
        8: ']',
        16: 'enter',
        32: 'left ctrl',
        64: 'a',
        128: 's',
    },
    5: {
        1: 'd',
        2: 'f',
        4: 'g',
        8: 'h',
        16: 'j',
        32: 'k',
        64: 'l',
        128: ';',
    },
    6: {
        1: '\'',
        2: '`',
        4: 'left shift',
        8: '\\',
        16: 'z',
        32: 'x',
        64: 'c',
        128: 'v',
    },
    7: {
        1: 'b',
        2: 'n',
        4: 'm',
        8: ',',
        16: '.',
        32: '/',
        64: 'right shift',
        128: 'keypad *',
    },
    8: {
        1: 'left alt',
        2: 'spacebar',
        4: 'capslock',
        8: 'f1',
        16: 'f2',
        32: 'f3',
        64: 'f4',
        128: 'f5',
    },
    9: {
        1: 'f6',
        2: 'f7',
        4: 'f8',
        8: 'f9',
        16: 'f10',
        32: 'keypad bloqnum',
        128: 'keypad 7',
    },
    10: {
        1: 'keypad 8',
        2: 'keypad 9',
        4: 'keypad -',
        8: 'keypad 4',
        16: 'keypad 5',
        64: 'keypad +',
        32: 'keypad 6',
        128: 'keypad 1',
    },
    11: {
        1: 'keypad 2',
        2: 'keypad 3',
        4: 'keypad 0',
        8: 'keypad .',
        64: '<',
        128: 'f11',
    },
    12: {
        1: 'f12',
    },
    13: {
        1: 'keypad intro',
        2: 'right ctrl',
        4: 'keypad /',
        8: 'printscreen',
        16: 'right alt',
        64: 'home',
        128: 'up',
    },
    14: {
        1: 'repag',
        2: 'left',
        4: 'right',
        8: 'end',
        16: 'down',
        32: 'avpag',
        64: 'insert',
        128: 'delete',

    },
    16: {
        32: 'left super',
        128: 'right super',
    },
}

modifiers = (
    'left shift',
    'right shift',
    'left ctrl',
    'right ctrl',
    'left alt',
    'right alt',
    'left super',
    'right super',
)

spanish_layout = {
    'wo_mods': {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'i': 'i',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'n': 'n',
        ';': 'ñ',
        'o': 'o',
        'p': 'p',
        'q': 'q',
        'r': 'r',
        's': 's',
        't': 't',
        'u': 'u',
        'v': 'v',
        'w': 'w',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'keypad 0': '0',
        'keypad 1': '1',
        'keypad 2': '2',
        'keypad 3': '3',
        'keypad 4': '4',
        'keypad 5': '5',
        'keypad 6': '6',
        'keypad 7': '7',
        'keypad 8': '8',
        'keypad 9': '9',
        'keypad .': '.',
        'keypad /': '/',
        'keypad *': '*',
        'keypad -': '-',
        'keypad +': '+',
        'keypad intro': '<intro>',
        'spacebar': '<spacebar>',
        'esc': 'esc',
        'backspace': '<backspace>',
        'delete': '<delete>',
        '`': 'º',
        '-': '\'',
        '=': '¡',
        '<': '<',
        'enter': '<enter>',
        '[': '`',
        ']': '+',
        '\'': '´',
        '\\': 'ç',
        ',': ',',
        '.': '.',
        '/': '-',
    },
    'shift': {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'h': 'H',
        'i': 'I',
        'j': 'J',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        ';': 'Ñ',
        'o': 'O',
        'p': 'P',
        'q': 'Q',
        'r': 'R',
        's': 'S',
        't': 'T',
        'u': 'U',
        'v': 'V',
        'w': 'W',
        'x': 'X',
        'y': 'Y',
        'z': 'Z',
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
        '-': '_',
        '=': '+',
        '<': '>',
        '[': '^',
        ']': '*',
        '\'': '¨',
        '\\': 'Ç',
        ',': ';',
        '.': ':',
        '/': '_',
    },
    'right_alt': {
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
