#!/usr/bin/python3

import ctypes
import json
import os
import sys
from ctypes.util import find_library
from time import sleep

assert("linux" in sys.platform)

x11 = ctypes.cdll.LoadLibrary(find_library("X11"))

display = x11.XOpenDisplay(None)

# This contains the keyboard state.
# 32 bytes, with each bit representing the state for a single key.
raw_keyboard = (ctypes.c_char * 32)()

key_mappings_container = {
    1: {
        2: '<esc>',
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
        64: '<backspace>',
        128: '<tab>',
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
        16: '<enter>',
        32: '<left ctrl>',
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
        4: '<left shift>',
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
        64: '<right shift>',
        128: '<unidentified>',
    },
    8: {
        1: '<left alt>',
        2: '<space bar>',
        4: '<caps lock>',
    },
    13: {
        2: '<right ctrl>',
        16: '<right alt>',
    },
}

modifiers = ('<left shift>', '<left ctrl>', '<left alt>', '<right shift>',
             '<right ctrl>', '<right alt>',)

last_keys = dict(modifiers=[], regular=[])


def x11_get_raw_keyboard():
    x11.XQueryKeymap(display, raw_keyboard)
    return raw_keyboard


def transform_keyboard(keyboard):
    try:
        keyboard = [ord(byte) for byte in keyboard]
        keyboard = enumerate(keyboard)
    except TypeError:
        return None

    return keyboard


def get_keys(keyboard):
    keys = dict(modifiers=[], regular=[])

    # loop on keyboard bytes
    for kb_byte_index, kb_byte in keyboard:
        try:
            key_mappings = key_mappings_container[kb_byte_index]
        except KeyError:
            continue

        # loop on key_mappings for that keyboard byte
        for key, value in key_mappings.items():
            if not kb_byte & key:
                continue
            elif value in modifiers:
                keys['modifiers'].append(value)
            elif not keys['regular']:
                keys['regular'].append(value)

    return keys


def run(sleep_time=.005, cb=print):
    while True:
        global last_keys

        sleep(sleep_time)
        raw_keyboard = x11_get_raw_keyboard()
        keyboard = transform_keyboard(raw_keyboard)

        if not keyboard:
            continue

        keys = get_keys(keyboard)

        if (keys['regular'] and keys['regular'] != last_keys['regular']):
            cb(keys)

        last_keys = keys


if __name__ == '__main__':
    run()
