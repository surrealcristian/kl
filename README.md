# kl

Simple keylogger for Linux + X11.


## Requirements

- Python 3
- xlib


## Installation

Install the latest stable release with `pip install kl` or download
[kl.py](https://raw.githubusercontent.com/surrealists/kl/master/kl.py) (unstable)
into your project directory.


## CLI usage

    usage: kl.py [-h] [-s SLEEP_TIME] [-t {spanish,english_usa,pt_br}] [-f FILE]
                 [-l]

### Examples:

Running kl.py without arguments, will print the pressed keys to stdout:

    $ ./kl.py

    # Type "example":

    {'regular': ['e'], 'modifiers': []}
    {'regular': ['x'], 'modifiers': []}
    {'regular': ['a'], 'modifiers': []}
    {'regular': ['m'], 'modifiers': []}
    {'regular': ['p'], 'modifiers': []}
    {'regular': ['l'], 'modifiers': []}
    {'regular': ['e'], 'modifiers': []}

Running kl.py using the `spanish` transformer, and writing to a file:

    ./kl.py -t spanish -f /tmp/kl.log

    # Type "ñandú":

    $ cat /tmp/kl.log
    ñ
    a
    n
    d
    ´
    u


## Layouts

`kl` comes with transformers for the next keyboard layouts:

- `english_usa`
- `spanish`
- `pt_br` (brazilian portuguese)


## Using `kl` as a library

`kl` can also be used as a library. For example:

```python
from kl import Kl, FileHandler, SpanishTransformer

transformer = SpanishTransformer()
handler = FileHandler(open('/tmp/kl.log', mode='w', buffering=1))

kl = Kl(sleep_time=0.01, transformer=transformer, handler=handler)
kl.run()
```


## License

MIT
