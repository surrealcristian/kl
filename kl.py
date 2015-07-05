#!/usr/bin/env python3

from __future__ import print_function

import ctypes
import sys
from ctypes.util import find_library
from time import sleep

if not 'linux' in sys.platform:
    raise RuntimeError('Platform not supported (Linux only).')

if not find_library('X11'):
    raise RuntimeError('X11 library is required.')

x11 = ctypes.cdll.LoadLibrary(find_library("X11"))

display = x11.XOpenDisplay(None)

# This contains the keyboard state.
# 32 bytes, with each bit representing the state for a single key.
raw_keymap = (ctypes.c_char * 32)()

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
        2: 'space bar',
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
        32: 'super left',
        128: 'super right',
    },
}

modifiers = (
    'left shift',
    'left ctrl',
    'left alt',
    'right shift',
    'right ctrl',
    'right alt',
)

last_keys = dict(modifiers=[], regular=[])
last_keymap = None


def get_keymap():
    """Returns X11 Keymap as a list of integers"""
    x11.XQueryKeymap(display, raw_keymap)

    try:
        keyboard = [ord(byte) for byte in raw_keymap]
    except TypeError:
        return None

    return keyboard


def get_keys(keymap):
    """Extract keys pressed from transformed keymap"""
    keys = dict(modifiers=[], regular=[])

    # loop on keymap bytes
    for keymap_index, keymap_byte in enumerate(keymap):
        try:
            keymap_values = keymap_values_list[keymap_index]
        except KeyError:
            continue

        # loop on keymap_values for that keymap byte
        for key, value in keymap_values.items():
            if not keymap_byte & key:
                continue
            elif value in modifiers:
                keys['modifiers'].append(value)
            elif not keys['regular']:
                keys['regular'].append(value)

    return keys


def run(sleep_time=.02, cb=print):
    """Main loop.
       Apply callback to the keys extracted"""
    while True:
        global last_keymap
        global last_keys

        sleep(sleep_time)

        keymap = get_keymap()

        if keymap == last_keymap or not keymap:
            continue

        keys = get_keys(keymap)

        if keys['regular'] and keys['regular'] != last_keys['regular']:
            cb(keys)

        last_keymap = keymap
        last_keys = keys


if __name__ == '__main__':
    run()
