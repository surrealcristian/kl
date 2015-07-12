# kl

Simple keylogger for Linux + X11.

## Requirements

- python 2 or 3
- xlib

## Installation

    pip install kl

## Usage

Using default parameters, the main loop sleep 2 centiseconds between
iterations, not transforms keys structure, and outputs to STDOUT.

```python
import kl

kl.run()
```

Changing the main loop sleep time to 1 centisecond, adding a callback to add a
timestamp to the structure, and writing it to disk.

```python
import json
import kl
import time


def add_time(keys):
    keys['timestamp'] = time.time()
    return keys


def log(keys):
    with open('/tmp/kl.log', 'a') as f:
        f.write(json.dumps(keys) + '\n')


kl.run(sleep_time=.01, transform=add_time, output=log)
```

## Transformers

`kl` comes with functions that apply a certain language layout to pressed
keys.

For example:

```python
import kl
from kl.transformers import spanish

kl.run(transform=spanish)
```

Actually the language layouts implemented are:

- `english_usa` (in progress)
- `spanish`
