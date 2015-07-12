from __future__ import print_function

import ctypes
import sys
from .data import keymap_values_list, modifiers
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


def run(sleep_time=.02, transform=None, output=print):
    """Main loop"""
    while True:
        global last_keymap
        global last_keys

        sleep(sleep_time)

        keymap = get_keymap()

        if keymap == last_keymap or not keymap:
            continue

        keys = get_keys(keymap)

        if keys['regular'] and keys['regular'] != last_keys['regular']:
            if transform:
                transformed_keys = transform(keys)
                if transformed_keys is not None:
                    output(transformed_keys)
            else:
                output(keys)

        last_keymap = keymap
        last_keys = keys
