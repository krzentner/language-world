

and write if-statements so that the robot can unplug the peg.

## Dialogue 2

- We are almost done!  There are 4 more tasks.  Please write a program to perform the task, `button-press-leftright`.
- Begin with the text:

```
# button-press-leftright: push the button from the side
def button_press_leftright(robot):
```

and write if-statements so that the robot can press the button.

## Dialogue 3

- We are almost done!  There are 3 more tasks.  Please write a program to perform the task, `window-close`.
- Begin with the text:

```
# window-close: slide the window closed to the right
def window_close(robot):
```

and write if-statements so that the robot can close the window.

## Dialogue 4

- We are almost done!  There are 2 more tasks.  Please write a program to perform the task, `pick-place`.
- Begin with the text:

```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
```

and write if-statements so that the robot can pick and place the puck.

## Dialogue 5

- We are almost done!  There is only one task left.  Please write a program to perform the task, `push`.
- Begin with the text:

```
# push: slide the puck to the target location
def push(robot):
```

and write if-statements so that the robot can push the puck.

"""[eod] [code]import os
import pathlib
import shutil
import sys
import tempfile
from typing import Iterable, Tuple, Union


class TemporaryDirectory:
    def __init__(self,
                 suffix: str = '',
                 prefix: str = 'temp',
                 dir: Union[str, pathlib.Path, None] = None,
                 delete: bool = True,
                 _preserve_cwd: bool = True):
        """Create a temporary directory and return its path.

        The directory will be removed upon Python exit, except if
        explicitly retained or specified with delete=False.

        The parameters are passed down to mkdtemp.

        :param suffix: Suffix of the temporary file names to create.
        :param prefix: Prefix of the temporary file names to create.
        :param dir: Directory (a string or object with a `path` property)
            in which the temporary directory should be created.
            If None, then the temporary directory will