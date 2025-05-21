+++
date = '2025-05-19T16:31:49-04:00'
draft = true
title = 'Typer and __init__'
tags = ['python', 'typer', 'dataclasses', 'dataclass', 'cli']
+++
Use Typer to turn classes into CLIs.

<!--more-->

### Typer

[Typer](https://typer.tiangolo.com/) is a fantastic python library for quickly
turning functions into CLIs, built by the folks behind
[FastAPI](https://fastapi.tiangolo.com/).  A minimal example:

```python
import typer


def add(a: float, b: float) -> float:
    '''Adds two numbers and returns the results'''
    return a + b


if __name__ == '__main__':
    typer.run(add)
```

There are loads more patterns and examples in the [official
documentation](https://typer.tiangolo.com/).

### \_\_init\_\_

If you'd like, you can serve a class with a typed `__init__` method:

```python
import typer


class Addor:
    '''Addor: Adds two numbers and print the result'''
    def __init__(self, a: float, b: float):
        print(a + b)


if __name__ == '__main__':
    typer.run(Addor)
```

### dataclasses

I love this pattern for defining CLI commands with dataclasses.  The
parameters and type info are all up front.  Defaults are clear and legible.
Personally I think this reads really cleanly.

```python
import dataclasses

import typer


@dataclasses.dataclass
class Addor:
    '''Addor: Adds two numbers and print the result'''
    a: float
    b: float

    def __post_init__(self):
        print(self.a + self.b)


if __name__ == '__main__':
    typer.run(Addor)
```

### typer.Typer

In case you were wondering, this works as well:

```python
import dataclasses

import typer


app = typer.Typer()

@app.command()
@dataclasses.dataclass
class Addor:
    '''Addor: Adds two numbers and print the result'''
    a: float
    b: float

    def __post_init__(self):
        print(self.a + self.b)


if __name__ == '__main__':
    app()
```
