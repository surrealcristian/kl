# kl

Simple keylogger for Linux + X11.

## Requirements

- python 2 or 3
- xlib

## Installation

    pip install kl

## Usage

Without custom callback (prints to STDOUT):

```python
import kl

kl.run()
```

With custom callback, logging to disk:

```python
import json
import kl

def log(keys):
    with open('/tmp/kl.log', 'a') as f:
        f.write(json.dumps(keys) + '\n')

kl.run(cb=log)
```
