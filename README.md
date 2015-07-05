# kl

Simple keylogger for Linux + X11.

## Requirements

- Python 3
- Xlib

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
        print(json.dumps(keys), file=f)

kl.run(cb=log)
```
